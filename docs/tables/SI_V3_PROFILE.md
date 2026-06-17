# SI_V3_PROFILE

> Stores the interaction names and version for HL7 V3 profiles.

**Description:** SI V3 Profile  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CERN_DEFINED_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the row is data set by Cerner or by client. 0 = client defined 1 = Cerner defined Other values may be added in the future. |
| 2 | `INTERACTION_NAME` | VARCHAR(20) | NOT NULL |  | Interaction name without the version |
| 3 | `INTERACTION_NAME_FULL` | VARCHAR(20) | NOT NULL |  | Interaction name with the version. |
| 4 | `PROFILE_EXTENSION` | VARCHAR(50) |  |  | The extension attribute of the profile Id |
| 5 | `PROFILE_ROOT` | VARCHAR(250) |  |  | The root attribute of the profile Id |
| 6 | `RECV_RESP_INTERACTION` | VARCHAR(20) | NOT NULL |  | The name of the receiver responsibility interaction without version. |
| 7 | `RECV_RESP_INT_FULL` | VARCHAR(20) | NOT NULL |  | The name of the receiver responsibility interaction with version. |
| 8 | `SI_V3_PROFILE_ID` | DOUBLE | NOT NULL |  | Primary key for the table.Column |
| 9 | `TDB_NBR` | DOUBLE |  |  | The tdb number to be used for the given request |
| 10 | `TRIGGER_TYPE_STR` | VARCHAR(15) |  |  | Lists the trigger type used to signal a given request |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VERSION_CODE` | VARCHAR(20) |  |  | Version code stringColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

