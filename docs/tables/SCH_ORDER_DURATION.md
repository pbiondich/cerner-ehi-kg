# SCH_ORDER_DURATION

> Scheduling Order Duration

**Description:** Scheduling Order Duration  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 41

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ARRIVAL_UNITS` | DOUBLE | NOT NULL |  | The arrival units. This provides a quantity (1,2,3?) |
| 6 | `ARRIVAL_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the units used in ARRIVAL_UNITS. (minutes, hours, etc.) |
| 7 | `ARRIVAL_UNITS_MEANING` | VARCHAR(12) |  |  | A 12 character description corresponding to ARRIVAL_UNITS_CD. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 10 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the order catalog entry. |
| 11 | `CLEANUP_UNITS` | DOUBLE | NOT NULL |  | Cleanup Duration Units |
| 12 | `CLEANUP_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the cleanup duration units of measure. |
| 13 | `CLEANUP_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the cleanup duration units of measure. |
| 14 | `DURATION_UNITS` | DOUBLE | NOT NULL |  | Duration Units |
| 15 | `DURATION_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the duration units of measure. |
| 16 | `DURATION_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the duration units of measure. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The field identifies the current permanent location of the patient. |
| 19 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 20 | `OFFSET_BEG_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset Beg Units |
| 21 | `OFFSET_BEG_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the beg units of measure. |
| 22 | `OFFSET_BEG_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the beg units of measure. |
| 23 | `OFFSET_END_UNITS` | DOUBLE | NOT NULL |  | Scheduling Offset End Units |
| 24 | `OFFSET_END_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the end units of measure. |
| 25 | `OFFSET_END_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the end offset units of measure. |
| 26 | `OFFSET_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier for the offset type. |
| 27 | `OFFSET_TYPE_MEANING` | VARCHAR(12) |  |  | A 12-char description corresponding to the offset type. |
| 28 | `RECOVERY_UNITS` | DOUBLE | NOT NULL |  | Recovery Duration |
| 29 | `RECOVERY_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The unique identifier for the recovery duration units of measure. |
| 30 | `RECOVERY_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the recovery duration units of measure. |
| 31 | `SCH_FLEX_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the scheduling flex string. |
| 32 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Determines the order of the object within a collection. |
| 33 | `SETUP_UNITS` | DOUBLE | NOT NULL |  | Setup Duration Units |
| 34 | `SETUP_UNITS_CD` | DOUBLE | NOT NULL | FK→ | The coded identifier of the setup duration units (minutes, hours, etc.) |
| 35 | `SETUP_UNITS_MEANING` | VARCHAR(12) |  |  | A 12-character description corresponding to the setup duration units. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 41 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ARRIVAL_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CATALOG_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `CLEANUP_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `DURATION_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LOCATION_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_BEG_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_END_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `OFFSET_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `RECOVERY_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SCH_FLEX_ID` | [SCH_FLEX_STRING](SCH_FLEX_STRING.md) | `SCH_FLEX_ID` |
| `SETUP_UNITS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

