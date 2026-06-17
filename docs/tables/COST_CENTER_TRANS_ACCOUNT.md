# COST_CENTER_TRANS_ACCOUNT

> Assigns cost centers to specific transaction types.

**Description:** COST CENTER TRANS ACCOUNT  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COST_CENTER_TRANS_ACCOUNT_ID` | DOUBLE | NOT NULL |  | The identifier assigned to the cost center transaction account.. |
| 2 | `LOCATION_CD` | DOUBLE | NOT NULL |  | The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed. |
| 3 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 4 | `TRANS_COST_CENTER_CD` | DOUBLE | NOT NULL |  | The General Ledger Cost Center where this type of transaction will be charged for the selected location. |
| 5 | `TRANS_SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The general ledger sub account code or expense category that this additional amount will be charged to. |
| 6 | `TRANS_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The Transaction Sub Type Code is also known as a Transaction Reason Code. These Reason Codes allow you to define different reasons for transactions and code them to different general ledger accounts. For example an adjustment to inventory due to price changes might be coded differently than adjustments to inventory due to flood damage. |
| 7 | `TRANS_TYPE_CD` | DOUBLE | NOT NULL |  | The transaction type code is used to identify different transactions such as transfer/issue, vendor returns, adjustments etc. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

