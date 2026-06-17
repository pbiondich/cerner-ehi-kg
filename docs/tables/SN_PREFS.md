# SN_PREFS

> This tables contains system preferences for SurgiNet applications

**Description:** SurgiNet Preferences  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity ID |
| 2 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Parent Entity Name |
| 3 | `PREF_DOMAIN` | VARCHAR(60) |  |  | Preference Domain |
| 4 | `PREF_ID` | DOUBLE | NOT NULL |  | Preference ID |
| 5 | `PREF_NAME` | VARCHAR(60) | NOT NULL |  | Preference Name |
| 6 | `PREF_SECTION` | VARCHAR(60) |  |  | Preference Section |
| 7 | `PREF_VALUE_CD` | DOUBLE | NOT NULL |  | Preference Value Code |
| 8 | `PREF_VALUE_DT_TM` | DATETIME |  |  | Preference Value Date/Time |
| 9 | `PREF_VALUE_ID` | DOUBLE | NOT NULL |  | Preference Value ID |
| 10 | `PREF_VALUE_NAME` | VARCHAR(32) |  |  | Preference Value Name |
| 11 | `PREF_VALUE_NBR` | DOUBLE |  |  | Preference Value Number |
| 12 | `PREF_VALUE_STR` | VARCHAR(255) |  |  | Preference Value String |
| 13 | `REFERENCE_IND` | DOUBLE | NOT NULL |  | Reference Indicator |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

