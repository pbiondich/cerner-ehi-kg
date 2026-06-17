# PFT_BR_EDIT_FAILURE

> Stores a list of claim scrubbing edit failures for a bill record.

**Description:** ProFit Bill Record Edit Failure  
**Table type:** ACTIVITY  
**Primary key:** `PFT_BR_EDIT_FAILURE_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL |  | Contains the Bill Version Number |
| 4 | `BO_HP_RELTN_ID` | DOUBLE |  | FK→ | Contains the ID of the balance on the BO_HP_RELTN table to which the edit failure is associated. |
| 5 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL |  | Identifies the bill record to which the edit is related. |
| 6 | `EDIT_DT_TM` | DATETIME | NOT NULL |  | The time the edit occurred. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EXTERNAL_GROUP_IDENT` | VARCHAR(250) | NOT NULL |  | The unique transaction external identifier from the cloud scrubbing service for this edit failure. |
| 9 | `EXT_PARTNER_IDENT` | VARCHAR(250) | NOT NULL |  | The identifier referencing this edit failure at an external claim scrubbing partner. |
| 10 | `FAILURE_INSTANCE_SEQ` | DOUBLE | NOT NULL |  | Indicates the sequence number for this edit failure. |
| 11 | `PFT_BR_EDIT_FAILURE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a claim scrubbing edit failure for a bill record. |
| 12 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the person who initiated the edit. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PFT_BR_EDIT_FAILURE_DETAIL](PFT_BR_EDIT_FAILURE_DETAIL.md) | `PFT_BR_EDIT_FAILURE_ID` |

