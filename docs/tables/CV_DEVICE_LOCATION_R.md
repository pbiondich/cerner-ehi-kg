# CV_DEVICE_LOCATION_R

> Stores the mappig between the Device name and Performing Location for which DBA has access to.

**Description:** CV DEVICE LOCATION RELATION  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_DEV_USER_IND` | DOUBLE | NOT NULL |  | It represents the active row for a given device based on the logged in user. |
| 2 | `CV_DEVICE_LOCATION_REF_ID` | DOUBLE | NOT NULL | FK→ | The Identifier of the Device Name - from the CV_DEVICE_LOCATION_REF table |
| 3 | `CV_DEVICE_LOCATION_R_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | Indicates if the device-performing location is set as a default. |
| 5 | `PERFORMING_LOCATION_CD` | DOUBLE | NOT NULL |  | Used to determine the code value associated in the codeset 220 |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `USER_ID` | DOUBLE | NOT NULL | FK→ | The Logged in user to powerchart who has Sign Privilege. This user id is different from updt_id. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CV_DEVICE_LOCATION_REF_ID` | [CV_DEVICE_LOCATION_REF](CV_DEVICE_LOCATION_REF.md) | `CV_DEVICE_LOCATION_REF_ID` |
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

