# COMMUNICATIONS_PORT

> The communications_port table defines the port characteristics of a specific port in a Delivery Class Queue.

**Description:** Communications Port  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 30

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_AREA_CODE` | CHAR(25) |  |  | Area Code of the station that the communications port is currently transmitting reports to. |
| 2 | `ACTIVE_COUNTRY_ACCESS` | CHAR(25) |  |  | Country Code of the station that the communications port is currently transmitting reports to I.e. the United States country code is 1. |
| 3 | `ACTIVE_DEST_CD` | DOUBLE | NOT NULL |  | Destination (Station) that is currently using the communications port. |
| 4 | `ACTIVE_EXCHANGE` | CHAR(25) |  |  | Phone Exchange of the station that the communications port is currently transmitting reports to. |
| 5 | `ACTIVE_PHONE_SUFFIX` | CHAR(50) |  |  | Phone Suffix of the station that the communications port is currently transmitting report to. |
| 6 | `AUTO_DIAL_IND` | DOUBLE |  |  | Indicates whether this communications port uses a leased line. |
| 7 | `DELIVERY_CLASS_QUEUE_ID` | DOUBLE | NOT NULL |  | Foreign Key into the Delivery Class Queue Table. Specifies which comm port is associated with a delivery class. |
| 8 | `DEVICE` | VARCHAR(50) |  |  | Currently not used. |
| 9 | `DEVICE_CD` | DOUBLE | NOT NULL |  | Foreign key into the device table. Indentifes what device is being sent to. |
| 10 | `DISABLED_IND` | DOUBLE |  |  | Indicates whether or not this communications port is disabled. |
| 11 | `KILL_ACTIVE_IND` | DOUBLE |  |  | Indicates whether to kill the current process |
| 12 | `MODEM_TYPE_ID` | DOUBLE | NOT NULL |  | The type of Modem used by this port. Foreign key into the modem_type table |
| 13 | `PORT_AREA_CODE` | CHAR(10) |  |  | The area code for this port |
| 14 | `PORT_COUNTRY_ACCESS` | CHAR(3) |  |  | The Country Access for this port |
| 15 | `PORT_EXCHANGE` | CHAR(10) |  |  | The exchange for this port |
| 16 | `PORT_PHONE_SUFFIX` | CHAR(30) |  |  | The phone suffix for this port |
| 17 | `PREFIX_DIAL_STRING` | CHAR(25) |  |  | The local prefix dial string, if any, for this port |
| 18 | `PREFIX_LONG_DISTANCE` | VARCHAR(25) |  |  | The long distance prefix dial string, if any, for this port |
| 19 | `PREFIX_MANUAL` | VARCHAR(25) |  |  | The manual prefix dial string, if any, for this port |
| 20 | `PREFIX_METRO` | VARCHAR(25) |  |  | The metro prefix dial string, if any, for this port |
| 21 | `STATUS` | DOUBLE |  |  | Current status of the communications port. |
| 22 | `SUFFIX_DIAL_STRING` | CHAR(25) |  |  | The local suffix dial string, if any, for this port |
| 23 | `SUFFIX_LONG_DISTANCE` | VARCHAR(25) |  |  | The long distance suffix dial string, if any, for this port |
| 24 | `SUFFIX_MANUAL` | VARCHAR(25) |  |  | The manual suffix dial string, if any, for this port |
| 25 | `SUFFIX_METRO` | VARCHAR(25) |  |  | The metro suffix dial string, if any, for this port |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

