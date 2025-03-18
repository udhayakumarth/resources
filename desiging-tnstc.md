Desiging TNSTC

buses table
-----------
id
regNo
chassiNo
EngNo
type
seats
region
health [HEALTHY, UNDER_SERVICE, UNDER_REGISTRATION, UNDER_INSPECTION, REQUIRE_SERVICE, REQUIRE_INSPECTION]
status
createdAt
updatedAt


bus_type table
--------------
id
name
descriptions
additionalFare


employee table
------------
id
name
email
mobile
dob
joiningDate
image
type [DRIVER, TICKTER, ETC..]

coustomer table
---------------

routes table
------------

booking table
-------------








--------------------------------------------------------
- Bus Deatils
Vehicle Type
Model
Year of Manufacture
Seating Capacity
Standing Capacity
Color
noOfDoors
noOfWheels
Engine
Dimension
Saftey
Technology
Warranty

- Engine Details
engineType
fuelType
fuelTankCapacity
Horsepower
Torque
transmissionType
Range

- Dimension Details
Length
Width
Height
Wheelbase
Curb Weight
GVWR(Gross Vehicle Weight Rating)

- Saftey Details 
Safety Standards
Braking System
isWheelchairAccessable

- Technology Details
GPS
Ticketing Systems
Digital Displays
CCTV Cameras
Climate Control


- Warranty Details

- Registration Details

- Insurance Details

- Inspection Reports

- Service History

- Manufacturer Details


bus_sevice
depo_service
staff_service
route_service
booking_service
