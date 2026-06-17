# MM_AP_LOG_LINE_HMW

> AP Log Line

**Description:** AP Log Line  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPANY_CODE` | VARCHAR(20) |  |  | Company Code |
| 2 | `COST_CENTER` | VARCHAR(60) |  |  | Cost Center number |
| 3 | `COST_CENTER_CD` | DOUBLE | NOT NULL |  | Cost Center codevalue |
| 4 | `EXTENDED_AMT` | DOUBLE |  |  | Extended Amount |
| 5 | `HEADER_ID` | DOUBLE | NOT NULL |  | Foreign Key |
| 6 | `INVOICE_LINE_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Invoice line item |
| 7 | `INVOICE_LINE_NBR` | DOUBLE |  |  | Invoice line number |
| 8 | `ITEM_DESC` | VARCHAR(100) |  |  | Item description |
| 9 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The unique id for the item master. |
| 10 | `LINE_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization ID |
| 12 | `PO_NBR` | VARCHAR(40) |  |  | PO Number |
| 13 | `PURCHASE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Purchase order ID |
| 14 | `RAW_DIST_LINE` | VARCHAR(200) |  |  | Raw line written to file. |
| 15 | `RAW_VOUCHER_LINE` | VARCHAR(200) |  |  | Raw voucher line |
| 16 | `SUB_ACCOUNT` | VARCHAR(60) |  |  | Sub Account |
| 17 | `SUB_ACCOUNT_CD` | DOUBLE | NOT NULL |  | Sub Account codevalue |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVOICE_LINE_ITEM_ID` | [INVOICE_LINE_ITEM](INVOICE_LINE_ITEM.md) | `INVOICE_LINE_ITEM_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PURCHASE_ORDER_ID` | [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PURCHASE_ORDER_ID` |

