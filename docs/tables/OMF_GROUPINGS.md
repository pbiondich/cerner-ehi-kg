# OMF_GROUPINGS

> OMF groupings such as physicians, procedures, shifts, and locations.

**Description:** OMF GROUPINGS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GROUPING_CD` | DOUBLE | NOT NULL |  | Code value of the group type (e.g. UM PHYSICIANS, SMR LOCATIONS) |
| 2 | `GROUPING_STATUS_CD` | DOUBLE | NOT NULL |  | Status of 'ACTIVE' or 'INACTIVE'. |
| 3 | `KEY1` | VARCHAR(200) | NOT NULL |  | Key 1 value. Typically the code_value, person_id, nomenclature_id that is being grouped. |
| 4 | `KEY2` | VARCHAR(200) |  |  | Key 2 value. Typically the code value of the group that the item is in. |
| 5 | `KEY3` | VARCHAR(200) |  |  | Key 3 value. Not used. |
| 6 | `KEY4` | VARCHAR(200) |  |  | Key 4 value. Not used. |
| 7 | `NUM1` | DOUBLE |  |  | Num 1 value - e.g. the age in years, day, etc. that is being grouped. |
| 8 | `NUM2` | DOUBLE |  |  | Num 2 value - e.g. the age in years, day, etc. that is being grouped.. |
| 9 | `NUM3` | DOUBLE |  |  | Num 3 value. Not used. |
| 10 | `NUM4` | DOUBLE |  |  | Num 4 value. Not used. |
| 11 | `OMF_GROUPING_ID` | DOUBLE | NOT NULL |  | Unique id of group/item combination. |
| 12 | `STRING1` | VARCHAR(200) |  |  | String value 1. |
| 13 | `STRING2` | VARCHAR(200) |  |  | String value 2. |
| 14 | `STRING3` | VARCHAR(200) |  |  | String value 3. |
| 15 | `STRING4` | VARCHAR(200) |  |  | String value 4. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VALID_FROM_DT_TM` | DATETIME |  |  | Start of when this grouping member is valid from. |
| 22 | `VALID_UNTIL_DT_TM` | DATETIME |  |  | End of when this grouping member is valid from. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

