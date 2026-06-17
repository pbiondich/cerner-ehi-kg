# TRACK_COMPLAINT

> Track Complaint

**Description:** List of Complaints (Lynx Problems) that can be assigned to a patient.  
**Table type:** REFERENCE  
**Primary key:** `TRACK_COMPLAINT_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `COMPLAINT_TITLE` | VARCHAR(255) |  |  | Textual display describing the Complaint (Lynx Problem) |
| 3 | `FOREIGN_COMPLAINT_ID` | DOUBLE | NOT NULL |  | Lynx Problem ID of the Lynx Problem matching this Complaint (Lynx Problem) |
| 4 | `PARENT_COMPLAINT_ID` | DOUBLE | NOT NULL |  | Track Complaint ID of the parent track complaint record. Used to define a problem hierarchy. |
| 5 | `TRACK_COMPLAINT_ID` | DOUBLE | NOT NULL | PK | Primary Key to the table. Sequence from i_tracking. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [TRACKING_COMPLAINT](TRACKING_COMPLAINT.md) | `TRACK_COMPLAINT_ID` |

