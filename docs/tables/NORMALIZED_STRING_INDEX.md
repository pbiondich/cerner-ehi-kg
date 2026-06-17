# NORMALIZED_STRING_INDEX

> Connects each individual word or phrase in any string to all its related strings.

**Description:** Normalized String Index  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The language that the string is expressed. |
| 8 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 9 | `NORMALIZED_STRING` | VARCHAR(255) |  |  | A normalized string is the result of breaking the string down into its constituent words, lower-casing each word, converting each word to its canonical form, and sorting the words in alphabetic order. |
| 10 | `NORMALIZED_STRING_A_NLS` | VARCHAR(1020) |  |  | NORMALIZED_STRING_A_NLS column |
| 11 | `NORMALIZED_STRING_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the normalized string index table. It is an internal system assigned number. |
| 12 | `NORMALIZED_STRING_NLS` | VARCHAR(255) |  |  | This column is used for non-English based strings with the NLSSORT function. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

