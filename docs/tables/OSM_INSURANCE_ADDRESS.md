# OSM_INSURANCE_ADDRESS

> The osm_insurance_address table contains the person, employer and the insurance addresses.

**Description:** OSM Insurance Address  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_INFO` | VARCHAR(30) |  |  | This is a free text field that contains additional osm insurance address information. |
| 2 | `ADDRESS` | VARCHAR(20) |  |  | This contains the address of the person, address, or insurance. |
| 3 | `CITY` | VARCHAR(15) |  |  | The city field is the text name of the city associated with the address row. |
| 4 | `HOME_PHONE` | VARCHAR(20) |  |  | This is the home phone number. |
| 5 | `OSM_INSURANCE_RELTN_ID` | DOUBLE | NOT NULL |  | This is the primary key of osm_insurance_address table. |
| 6 | `STATE` | VARCHAR(2) |  |  | The state field is the text name of the state or province associated with the address row. |
| 7 | `TYPE_FLAG` | DOUBLE | NOT NULL |  | This is the flag that indicate the address type of person, employer or insurance. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `WORK_PHONE` | VARCHAR(20) |  |  | This is the work phone number. |
| 14 | `ZIP` | VARCHAR(10) |  |  | This field contains the postal code for the street address in the address row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

