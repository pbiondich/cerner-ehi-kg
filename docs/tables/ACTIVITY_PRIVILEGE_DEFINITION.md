# ACTIVITY_PRIVILEGE_DEFINITION

> This table is used to define activities.

**Description:** Activity_Privilege_ Definition  
**Table type:** REFERENCE  
**Primary key:** `ACTIVITY_PRIVILEGE_DEF_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_IDENTIFIER` | VARCHAR(25) | NOT NULL |  | Identifier for the activity that is getting defined. |
| 3 | `ACTIVITY_NAME` | VARCHAR(255) | NOT NULL |  | Name descriptor for the activity. Identifies the name of the Activity. |
| 4 | `ACTIVITY_PRIVILEGE_DEF_ID` | DOUBLE | NOT NULL | PK | Primary key for the activity_privilege_ definition. The unique identifier of a row on this table |
| 5 | `ACTIVITY_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of the Activity. Indicates the type of activity, such as 1 for UK. This is used to classify the activity. 1 - Activity type is "UK" (Currently there is only one valid value) |
| 6 | `PRIVILEGE_CD` | DOUBLE | NOT NULL |  | Privilege_cd that is be to associated with the Activity |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ACTIVITY_PRIVILEGE_RELTN](ACTIVITY_PRIVILEGE_RELTN.md) | `ACTIVITY_PRIVILEGE_DEF_ID` |
| [PRIVILEGE_DELETION](PRIVILEGE_DELETION.md) | `ACTIVITY_PRIVILEGE_DEF_ID` |

