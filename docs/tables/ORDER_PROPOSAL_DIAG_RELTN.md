# ORDER_PROPOSAL_DIAG_RELTN

> This table stores attributes that are a part of the relationship between the Order _Proposal and Diagnosis tables.

**Description:** Order Proposal Diagnosis Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DIAGNOSIS_ALTER_FLAG` | DOUBLE | NOT NULL |  | Identifies what type of diagnosis change it is. For a proposal to create an order this field is set to 1, which indicates it is a new diagnosis. 0 - Unchanged, 1 - Add, 2 - Modify, 3 - Delete |
| 2 | `DIAGNOSIS_ID` | DOUBLE | NOT NULL | FK→ | This is the diagnosis ID from the Diagnosis table of the diagnosis associated with the order proposal. |
| 3 | `ORDER_PROPOSAL_DIAG_RELTN_ID` | DOUBLE | NOT NULL |  | This is the primary key of this table. It is assigned internally by the system. |
| 4 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | This is the ID of the order proposal associated to this diagnosis. |
| 5 | `RANK_SEQUENCE` | DOUBLE | NOT NULL |  | This field captures how the diagnosis is ranked in relationship to the order proposal. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DIAGNOSIS_ID` | [DIAGNOSIS](DIAGNOSIS.md) | `DIAGNOSIS_ID` |
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |

