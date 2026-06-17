# SA_PREFERENCE_VALUE

> Contains preference values used for anesthesia preferences Based on the number of SA_PREFERENCE rows. Estimate 50:1 with SA_PREFERENCE. 5,000

**Description:** SA Preference Values  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | For PREFERENCE_VALUE_TYPE_FLAG of ID, contains the id of the preference value |
| 6 | `PARENT_ENTITY_NAME` | CHAR(50) | NOT NULL |  | For PREFERENCE_VALUE_TYPE_FLAG of ID, contains the table name of where the id comes from |
| 7 | `PREFERENCE_VALUE` | VARCHAR(250) |  |  | The value of the preference |
| 8 | `PREFERENCE_VALUE_NAME` | VARCHAR(250) |  |  | The name of preference that is being set |
| 9 | `PREFERENCE_VALUE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of value that PREFERENCE_VALUE is (string, number, date, etc.) |
| 10 | `SA_PREFERENCE_ID` | DOUBLE | NOT NULL | FK→ | The parent Preference group that this value belongs to |
| 11 | `SA_PREFERENCE_VALUE_ID` | DOUBLE | NOT NULL |  | Unique value that identifies the preference value |
| 12 | `SEQUENCE` | DOUBLE |  |  | SEQUENCE - The sequence this preference setting should be displayed in |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SA_PREFERENCE_ID` | [SA_PREFERENCE](SA_PREFERENCE.md) | `SA_PREFERENCE_ID` |

