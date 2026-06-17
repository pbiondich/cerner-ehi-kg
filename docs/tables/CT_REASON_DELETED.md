# CT_REASON_DELETED

> Stores the information on why enrollment information has been logically deleted.

**Description:** Clinical Trials - Reason Deleted  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CONSENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique consent that has been logically deleted. |
| 6 | `CT_REASON_DEL_ID` | DOUBLE | NOT NULL |  | Primary Key. From Sequence PROTOCOL_DEF_SEQ |
| 7 | `DELETION_DT_TM` | DATETIME | NOT NULL |  | The date and time the deletion occurred. |
| 8 | `DELETION_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person who performed the deletion. |
| 9 | `DELETION_REASON` | VARCHAR(2000) | NOT NULL |  | The reason why the deletion was done. Free Form text. |
| 10 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier from the PERSON table to indicate which patient has been deleted from the view. |
| 11 | `PROT_MASTER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the protocol on which the deletion of the patient is performed. |
| 12 | `PT_ELIG_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Pt_Elig_Tracking_Id. Foreign Key. |
| 13 | `REG_ID` | DOUBLE | NOT NULL |  | From table PT_PROT_REG. Not a Foreign Key |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONSENT_ID` | [PT_CONSENT](PT_CONSENT.md) | `PT_CONSENT_ID` |
| `DELETION_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PROT_MASTER_ID` | [PROT_MASTER](PROT_MASTER.md) | `PROT_MASTER_ID` |
| `PT_ELIG_TRACKING_ID` | [PT_ELIG_TRACKING](PT_ELIG_TRACKING.md) | `PT_ELIG_TRACKING_ID` |

