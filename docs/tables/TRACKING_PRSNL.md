# TRACKING_PRSNL

> Tracking table used to identify each provider assigned to a tracking group.

**Description:** Tracking Personnel Table  
**Table type:** ACTIVITY  
**Primary key:** `TRACKING_PRSNL_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AVAILABILITY_IND` | DOUBLE |  |  | An indicator used to define if the selected provider is available to assign to individual patients. |
| 3 | `DEF_ENCNTR_PRSNL_R_CD` | DOUBLE | NOT NULL | FK→ | The default relation code to set as the default relationship for this provider. |
| 4 | `DEF_LOCATION_CD` | DOUBLE | NOT NULL |  | Default Location CodeColumn |
| 5 | `DISPLAY_NAME` | VARCHAR(10) |  |  | Provider display name (default set to the provider initials)Column |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 7 | `REVIEW_IND` | DOUBLE |  |  | Indicates the provider could review a result or not within the tracking list.Column |
| 8 | `TRACKING_GROUP_CD` | DOUBLE | NOT NULL | FK→ | Tracking Group Code used to identify which tracking group this provider is associated with. |
| 9 | `TRACKING_PRSNL_COLOR` | VARCHAR(20) |  |  | Tracking Personnel ColorColumn |
| 10 | `TRACKING_PRSNL_COMMENT` | LONGTEXT |  |  | Tracking Personnel CommentColumn |
| 11 | `TRACKING_PRSNL_ID` | DOUBLE | NOT NULL | PK | Tracking Personnel Identifier |
| 12 | `TRACKING_PRSNL_TASK_ID` | DOUBLE | NOT NULL | FK→ | The associated provider task identifier from the tracking reference table. This identifier defines the task this provider is currently assigned to perform. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEF_ENCNTR_PRSNL_R_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TRACKING_GROUP_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TRACKING_PRSNL_TASK_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_PRSNL_REF](TRACKING_PRSNL_REF.md) | `TRACKING_PRSNL_ID` |

