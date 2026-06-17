# ORDER_PROPOSAL_THER_SBSTTN

> This table stores the therapeutic substitution information for an order proposal at the ingredient level. When a therapeutic substitution rule is accepted, overridden, or an alternate regimen is applied to an order proposal, a row will be added to this table.

**Description:** Order Proposal Therapeutic Substitution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMP_SEQUENCE` | DOUBLE | NOT NULL |  | System assigned number, identifying the order of the ingredient within the proposal where substitution occurred. |
| 2 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The ID of the order proposal associated with this substitution. |
| 3 | `ORDER_PROPOSAL_THER_SBSTTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_PROPOSAL_THER_SBSTTN table. |
| 4 | `OVERRIDE_REASON_CD` | DOUBLE | NOT NULL |  | Codified value for the reason the therapeutic substitution was overridden. When a therapeutic substitution is accepted or an alternate regiment is applied, this field will be 0. If the therapeutic substitution is overridden, this field must contain the reason code value. |
| 5 | `SUBSTITUTION_ACCEPT_FLAG` | DOUBLE | NOT NULL |  | The flag to indicate whether the therapeutic substitution was accepted or overridden. The possible values are 1 = accept, 2 = override, and 3 = alternate regimen. |
| 6 | `THERAP_SBSTTN_ID` | DOUBLE | NOT NULL |  | The ID of the therapeutic substitution rule applied to the order proposal. The field will be 0 if the substitution rule is overridden. If the substitution rule is accepted or an alternate regimen is applied, this field should contain a unique identifier from the rx_therap_sbsttn table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |

