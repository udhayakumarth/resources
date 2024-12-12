#!/bin/bash

# Input and output files
INPUT_FILE="input.txt"
OUTPUT_FILE="output.txt"
LOG_FILE="script.log"
TEMP_FILE="temp.ldif"

# Ensure output and log files are clean before running
> "$OUTPUT_FILE"
> "$LOG_FILE"

# Function to get the current timestamp
timestamp() {
  date +"%Y-%m-%d %H:%M:%S"
}

# Main processing loop
while read -r email; do
  # Skip empty lines
  if [[ -z "$email" ]]; then
    continue
  fi

  echo -e "\033[1;34mProcessing user: $email...\033[0m"
  echo "$(timestamp) | Processing user: $email" >> "$LOG_FILE"

  # Execute the dsearch command to get the user details
  result=$(dsearch -b "dc=web, dc=optus, dc=com, dc=au" \
    -D "cn=srauser, ou=system accounts, dc=web, dc=optus, dc=com, dc=au" \
    -w "Prd@001" -h localhost -p 1389 -LLL -s sub "(mail=$email)" \
    dn mail smLogin accountDisabled idmRole idmAdmin 2>>"$LOG_FILE")

  # Check if the user exists in the directory
  if [[ -z "$result" ]]; then
    echo "$(timestamp) | Error: User $email not found in directory." >> "$LOG_FILE"
    echo "$email - failed - $(timestamp)" >> "$OUTPUT_FILE"
    echo -e "\033[1;31mFailed: User $email not found.\033[0m"
    continue
  fi

  echo "$(timestamp) | Fetched details for $email:" >> "$LOG_FILE"
  echo "$result" >> "$LOG_FILE"
  echo "----------------------------------------" >> "$LOG_FILE"

  # Create LDIF file for dxmodify command
  echo "$result" | while read -r line; do
    if [[ "$line" =~ ^dn: ]]; then
      echo "$line" > "$TEMP_FILE"
      echo "$(timestamp) | Original: $line | Updated: $line" >> "$LOG_FILE"
    elif [[ "$line" =~ ^accountDisabled: ]]; then
      updated_line="accountDisabled: 2"
      echo "$updated_line" >> "$TEMP_FILE"
      echo "$(timestamp) | Original: $line | Updated: $updated_line" >> "$LOG_FILE"
    elif [[ "$line" =~ ^dc ]]; then
      echo "$line" >> "$TEMP_FILE"
      echo "$(timestamp) | Original: $line | Updated: $line" >> "$LOG_FILE"
    else
      attribute=$(echo "$line" | cut -d':' -f1)
      value=$(echo "$line" | cut -d':' -f2- | sed 's/^ //')
      updated_value="to_be_deleted$value"
      updated_line="$attribute: $updated_value"
      echo "$updated_line" >> "$TEMP_FILE"
      echo "$(timestamp) | Original: $line | Updated: $updated_line" >> "$LOG_FILE"
    fi
  done

  # Execute the dxmodify command
  dxmodify -f "$TEMP_FILE" 2>>"$LOG_FILE"
  if [[ $? -eq 0 ]]; then
    echo "$(timestamp) | Successfully updated user $email." >> "$LOG_FILE"
    echo "$email - successful - $(timestamp)" >> "$OUTPUT_FILE"
    echo -e "\033[1;32mSuccess: User $email updated.\033[0m"
  else
    echo "$(timestamp) | Error: Failed to update user $email." >> "$LOG_FILE"
    echo "$email - failed - $(timestamp)" >> "$OUTPUT_FILE"
    echo -e "\033[1;31mFailed: Could not update $email.\033[0m"
  fi

  echo "----------------------------------------" >> "$LOG_FILE"

  # Clean up temporary files
  rm -f "$TEMP_FILE"
done < "$INPUT_FILE"

echo -e "\033[1;36mAll tasks completed. Check $OUTPUT_FILE and $LOG_FILE for details.\033[0m"