# LH_QRDA_SOCIAL_HISTORY

> This table is used to store elements that are used to create the Social History Section in the body of a QRDA file for submission

**Description:** LH_QRDA_SOCIAL_HISTORY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EFFECTIVE_DT_TM` | DATETIME |  |  | Represents the time the social history was created/noted |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 7 | `LH_QRDA_SOCIAL_HISTORY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_SOCIAL_HISTORY table. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Problem section is related (i.e. lh_qrda_pqrs_id) |
| 10 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 11 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Problem section is related (i.e. LH_QRDA_PQRS) |
| 12 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 13 | `SHX_CODE` | VARCHAR(50) |  |  | The code associated with a social history result |
| 14 | `SHX_CODE_SYSTEM` | VARCHAR(50) |  |  | Represents the codeSystem string of the observation/code/@codesystem |
| 15 | `SHX_CODE_SYSTEM_NAME` | VARCHAR(100) |  |  | String Representation of Social History Code OID |
| 16 | `SHX_DISPLAY` | VARCHAR(500) |  |  | Text description of a social history result |
| 17 | `SHX_ID` | DOUBLE | NOT NULL |  | Unique social history id |
| 18 | `SHX_STATUS_CODE` | VARCHAR(50) |  |  | The code associated with a social history status value |
| 19 | `SHX_STATUS_DISPLAY` | VARCHAR(500) |  |  | Text description of a social history status value |
| 20 | `SHX_STATUS_TYPE` | VARCHAR(50) |  |  | The type of code associated with a given social history status value (e.g. SNOMED CT / CPT-4) |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

