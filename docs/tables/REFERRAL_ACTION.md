# REFERRAL_ACTION

> Tracks the changes to the status of a referral. Also tracks the personnel and date/times of the modification of the referral.

**Description:** Referral Action  
**Table type:** ACTIVITY  
**Primary key:** `REFERRAL_ACTION_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_DT_TM` | DATETIME |  |  | Date and time the referral was affected by the referral action. It can be defined by the user performing the action. |
| 2 | `ACTION_PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the Personnel ID of the user that performs the action. |
| 3 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 6 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that the row was created. |
| 8 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason for which the referral action was performed. |
| 9 | `REFERRAL_ACTION_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the REFERRAL_ACTION table. |
| 10 | `REFERRAL_ACTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of action that was performed on the referral. |
| 11 | `REFERRAL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related referral. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | `REFERRAL_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REFERRAL_CONTACT](REFERRAL_CONTACT.md) | `REFERRAL_ACTION_ID` |

