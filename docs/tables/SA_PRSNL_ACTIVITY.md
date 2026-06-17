# SA_PRSNL_ACTIVITY

> Contains records that document prsnl associated to an anesthesia record Based on the # of prsnl involved in a case, and how they are tracked. Estimate 3:1 with SA_ANESTHESIA_RECORD. 78,300

**Description:** SA Personnel Activity  
**Table type:** ACTIVITY  
**Primary key:** `SA_PRSNL_ACTIVITY_ID`  
**Columns:** 22  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CREATED_DT_TM` | DATETIME |  |  | Stores the date time at which personnel was added |
| 6 | `CREATED_ID` | DOUBLE | NOT NULL | FK→ | Stores ID of the user who added a personnel |
| 7 | `MAX_RES_CONCURRENCY_VAL` | DOUBLE | NOT NULL |  | The maximum Supervisor Conurrency for the provider on the record. |
| 8 | `MAX_SUP_CONCURRENCY_VAL` | DOUBLE | NOT NULL |  | The maximum Resident Conurrency value for this provider on the record |
| 9 | `PREVIOUS_PRSNL_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | The previous activity record that this record replaces (because of a change), if 0 this is the original record |
| 10 | `PRSNL_ACTIVITY_DT_TM` | DATETIME |  |  | The date/time the activity occurred |
| 11 | `PRSNL_ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | The type of activity that the activity record is documenting |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The provider that the activity record is documenting |
| 13 | `REFERRED_IN_SURGERY_IND` | DOUBLE |  |  | Indicates if surgery documentation recorded the attendee |
| 14 | `SA_ANESTHESIA_RECORD_ID` | DOUBLE | NOT NULL | FK→ | The anesthesia record that the prsnl activity is for |
| 15 | `SA_PRSNL_ACTIVITY_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the prsnl activity record |
| 16 | `SA_REF_CAT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | SA REFERENCE CATEGORY PERSONNEL ID FK TO SA_REF_CAT_PRSNL |
| 17 | `START_IND` | DOUBLE |  |  | Indicates whether this is defining a start or end time (1=start,0=end) |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PREVIOUS_PRSNL_ACTIVITY_ID` | [SA_PRSNL_ACTIVITY](SA_PRSNL_ACTIVITY.md) | `SA_PRSNL_ACTIVITY_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_ANESTHESIA_RECORD_ID` | [SA_ANESTHESIA_RECORD](SA_ANESTHESIA_RECORD.md) | `SA_ANESTHESIA_RECORD_ID` |
| `SA_REF_CAT_PRSNL_ID` | [SA_REF_CAT_PRSNL](SA_REF_CAT_PRSNL.md) | `SA_REF_CAT_PRSNL_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_PRSNL_ACTIVITY](SA_PRSNL_ACTIVITY.md) | `PREVIOUS_PRSNL_ACTIVITY_ID` |
| [SA_PRSNL_ACTIVITY_TIME](SA_PRSNL_ACTIVITY_TIME.md) | `SA_PRSNL_ACTIVITY_ID` |

