# SCH_QUOTA

> Scheduling quota data

**Description:** Scheduling quota  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 45

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `BEG_TM` | DOUBLE | NOT NULL |  | Defines the standard start time. |
| 7 | `DATA1_SOURCE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the scheduling data source. |
| 8 | `DATA1_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 9 | `DATA2_SOURCE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the scheduling data source. |
| 10 | `DATA2_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 11 | `DATA3_SOURCE_CD` | DOUBLE | NOT NULL |  | A coded identifier for the scheduling data source. |
| 12 | `DATA3_SOURCE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the scheduling data source. |
| 13 | `DAYS_OF_WEEK` | VARCHAR(7) |  |  | A character string used to store the valid days of the week. |
| 14 | `DISPLAY1_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 15 | `DISPLAY1_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID1 |
| 16 | `DISPLAY1_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID1 |
| 17 | `DISPLAY2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 18 | `DISPLAY2_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID2 |
| 19 | `DISPLAY2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID2 |
| 20 | `DISPLAY3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the display object. |
| 21 | `DISPLAY3_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the DISPLAY_ID3 |
| 22 | `DISPLAY3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the DISPLAY_ID3 |
| 23 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 24 | `END_TM` | DOUBLE | NOT NULL |  | Defines the standard ending time. |
| 25 | `OVERBOOK_LIMIT` | DOUBLE | NOT NULL |  | Overbook limit |
| 26 | `PARENT1_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 27 | `PARENT1_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT1_ID |
| 28 | `PARENT1_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT1_ID |
| 29 | `PARENT2_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 30 | `PARENT2_MEANING` | VARCHAR(12) |  |  | Parent2 Meaning |
| 31 | `PARENT2_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT2_ID |
| 32 | `PARENT3_ID` | DOUBLE | NOT NULL |  | The unique identifier of the parent object. |
| 33 | `PARENT3_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the PARENT3_ID |
| 34 | `PARENT3_TABLE` | VARCHAR(32) |  |  | The parent table corresponding to the PARENT3_ID |
| 35 | `QUOTA_LIMIT` | DOUBLE | NOT NULL |  | quota limit |
| 36 | `QUOTA_TYPE_CD` | DOUBLE | NOT NULL |  | quota type code |
| 37 | `QUOTA_TYPE_MEANING` | VARCHAR(12) | NOT NULL |  | quota type meaning |
| 38 | `QUOTA_TZ` | DOUBLE | NOT NULL |  | quota time zone |
| 39 | `SCH_QUOTA_ID` | DOUBLE | NOT NULL |  | Scheduling quota identifier |
| 40 | `TIME_RESTR_CD` | DOUBLE | NOT NULL |  | Time restriction code - AM, PM only etc, from code set 16153 |
| 41 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 42 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 43 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 44 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 45 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

