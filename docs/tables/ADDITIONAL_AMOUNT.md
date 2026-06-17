# ADDITIONAL_AMOUNT

> ADDITIONAL AMOUNT Table

**Description:** ADDITIONAL AMOUNT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_AMOUNT_ID` | DOUBLE | NOT NULL |  | The identifier assigned to the purchase order additional amount. |
| 2 | `ADDITIONAL_AMOUNT_TYPE_CD` | DOUBLE | NOT NULL |  | The code associated with the additional amount type. This might include Tax, Freight, Service Charges, VAT Tax, Deposit, Credit and so forth. |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | The General Ledger Cost Center where this transaction will be charged. |
| 4 | `CREATE_APPLCTX` | DOUBLE | NOT NULL |  | Creating Application Context |
| 5 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Created Date Time |
| 6 | `CREATE_ID` | DOUBLE | NOT NULL |  | Creator ID |
| 7 | `CREATE_TASK` | DOUBLE |  |  | Creating Task |
| 8 | `DOLLAR_AMOUNT` | DOUBLE |  |  | The dollar amount to be charged in association with this additional amount code. |
| 9 | `MATCHED_IND` | DOUBLE |  |  | Indicates if this additional amount has already been "matched" tp a purchase order. |
| 10 | `MM_PROJECT_NBR_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Link to the project used for the budget. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Parent Entity Table ID value |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | The name of the parent entity (table) |
| 13 | `REFERENCE` | VARCHAR(40) |  |  | Reference Text |
| 14 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | The general ledger sub account code or expense category that this additional amount will be charged to. |
| 15 | `TAX_AMOUNT` | DOUBLE |  |  | This field stores calculated header level and line level tax amount. |
| 16 | `TAX_IND` | DOUBLE |  |  | This indicator shows whether the additional amount is considered as a tax. |
| 17 | `TAX_TYPE_CD` | DOUBLE | NOT NULL |  | Tax Type code from code set 14066 |
| 18 | `TAX_VALUE` | DOUBLE | NOT NULL |  | Tax Value Amount |
| 19 | `TAX_VALUE_FLAG` | DOUBLE | NOT NULL |  | This flag indicates whether tax value is a percentage or fixed amount. 1 = Percentage; 2 = Fixed Amount; 0 = not assigned |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MM_PROJECT_NBR_TRACKING_ID` | [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `MM_PROJECT_NBR_TRACKING_ID` |

