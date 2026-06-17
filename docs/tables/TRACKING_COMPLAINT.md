# TRACKING_COMPLAINT

> Tracking Complaint

**Description:** Activity table listing the complaints (Lynx Problems) selected for a patient.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `PRIORITY_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence order in which the problem is presented in user interfaces. Indicates relative importance of the problem. |
| 4 | `TRACKING_COMPLAINT_ID` | DOUBLE | NOT NULL |  | Primary Key for the table. Sequenced from i_tracking. |
| 5 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL |  | Tracking Group the Patient is checked into. |
| 6 | `TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking ID (tracking_item key) of the patient. |
| 7 | `TRACK_COMPLAINT_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key pointing to the reference Track Complaint this record refers to. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `TRACK_COMPLAINT_ID` | [TRACK_COMPLAINT](TRACK_COMPLAINT.md) | `TRACK_COMPLAINT_ID` |

