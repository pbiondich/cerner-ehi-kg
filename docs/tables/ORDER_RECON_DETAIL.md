# ORDER_RECON_DETAIL

> Stores detailed information about each order that was reconciled by a user during the patient care venue changes.

**Description:** Order Reconciliation Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLINICAL_DISPLAY_LINE` | VARCHAR(2000) | NOT NULL |  | Clinical display line for the order at the time of reconciliation. |
| 2 | `CONTINUE_ORDER_IND` | DOUBLE | NOT NULL |  | Indicates whether the personnel that performed the reconciliation chose to continue the order. 1 - Continue the order, 2 - Do not continue the order, 3 - Continue the order with changes, 4 - acknowledge order. |
| 3 | `ORDER_MNEMONIC` | VARCHAR(1000) |  |  | The mnemonic for this order. |
| 4 | `ORDER_NBR` | DOUBLE | NOT NULL |  | The order ID for the reconciled order. |
| 5 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The proposal id for the reconciled proposal. |
| 6 | `ORDER_RECON_DETAIL_ID` | DOUBLE | NOT NULL |  | The primary key of this table. |
| 7 | `ORDER_RECON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order reconciliation that this detail is related to. |
| 8 | `RECON_NOTE_TXT` | VARCHAR(500) |  |  | This field will be used to store any reconciliation related note for an order. |
| 9 | `RECON_ORDER_ACTION_MEAN` | VARCHAR(20) | NOT NULL |  | The action that was taken on an order during the reconciliation process. |
| 10 | `SIMPLIFIED_DISPLAY_LINE` | VARCHAR(1000) |  |  | Simplified display line for the order at the time of reconciliation |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |
| `ORDER_RECON_ID` | [ORDER_RECON](ORDER_RECON.md) | `ORDER_RECON_ID` |

