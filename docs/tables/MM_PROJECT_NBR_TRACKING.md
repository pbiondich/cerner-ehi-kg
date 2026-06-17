# MM_PROJECT_NBR_TRACKING

> Stores information about Purchasing projects.

**Description:** Project Number Tracking  
**Table type:** REFERENCE  
**Primary key:** `MM_PROJECT_NBR_TRACKING_ID`  
**Columns:** 34  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `INVOICED_BUDGET_AMT` | DOUBLE | NOT NULL |  | Total amount invoiced against the budget. |
| 4 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 5 | `MM_PROJECT_NBR_TRACKING_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the MM_PROJECT_NBR_TRACKING table. |
| 6 | `PREV_MM_PROJECT_NBR_TRACK_ID` | DOUBLE | NOT NULL | FK→ | Contains the unique ID of the previous version of the current effective row. |
| 7 | `PROJECT_BUDGET_AMT` | DOUBLE | NOT NULL |  | The total budget allocated for the project. |
| 8 | `PROJECT_BUDGET_UPDT_IND` | DOUBLE | NOT NULL |  | Indicates if the project budget amount was updated on this row. |
| 9 | `PROJECT_DESC` | VARCHAR(60) | NOT NULL |  | Long description of the project. |
| 10 | `PROJECT_DESC_KEY` | VARCHAR(60) | NOT NULL |  | Upper case version of the project long description. |
| 11 | `PROJECT_DESC_KEY_A_NLS` | VARCHAR(240) | NOT NULL |  | Stores the corresponding non-English character set values for the PROJECT_DESC_KEY column. Used to sort correctly internationally. |
| 12 | `PROJECT_END_DT_TM` | DATETIME |  |  | The scheduled ending date and time for the project. |
| 13 | `PROJECT_NUMBER_TXT` | VARCHAR(40) | NOT NULL |  | Character representation of the identifying project number. |
| 14 | `PROJECT_NUMBER_TXT_KEY` | VARCHAR(40) | NOT NULL |  | Character representation of the identifying project number. |
| 15 | `PROJECT_NUMBER_TXT_KEY_A_NLS` | VARCHAR(160) | NOT NULL |  | Stores the corresponding non-English character set values for the project_number_txt column. Used to sort correctly internationally. |
| 16 | `PROJECT_SHORT_DESC` | VARCHAR(40) | NOT NULL |  | A short version of the description of the project. |
| 17 | `PROJECT_SHORT_DESC_KEY` | VARCHAR(40) | NOT NULL |  | Uppercase standardized version of the PROJECT_SHORT_DESC. |
| 18 | `PROJECT_SHORT_DESC_KEY_A_NLS` | VARCHAR(160) | NOT NULL |  | Stores the corresponding non-English character set values for the project_short_desc_key column. Used to sort correctly internationally. |
| 19 | `PROJECT_START_DT_TM` | DATETIME | NOT NULL |  | The date and time that a project begins. |
| 20 | `PURCHASED_BUDGET_AMT` | DOUBLE | NOT NULL |  | Total amount purchased against the budget. |
| 21 | `PURCHASE_ALERT_EMAIL` | VARCHAR(255) |  |  | The email addresses to alert when a single purchase order commit exceeds the limit set in purchase_amt. |
| 22 | `PURCHASE_AMT` | DOUBLE | NOT NULL |  | The limit set for notification when the value of a single PO committed is exceeded. |
| 23 | `RECEIVED_BUDGET_AMT` | DOUBLE | NOT NULL |  | Total amount received against the budget. |
| 24 | `TOTAL_INVOICE_ALERT_EMAIL` | VARCHAR(255) |  |  | The email addresses to alert when the sum of all invoices committed exceeds the limit set in total_invoice_amt. |
| 25 | `TOTAL_INVOICE_AMT` | DOUBLE | NOT NULL |  | The limit set for notification when the sum value of all invoices is exceeded. |
| 26 | `TOTAL_PURCHASE_ALERT_EMAIL` | VARCHAR(255) |  |  | The email addresses to alert when the sum of all purchases committed exceeds the limit set in total_purchase_amt. |
| 27 | `TOTAL_PURCHASE_AMT` | DOUBLE | NOT NULL |  | The limit set for notification when the sum value of all purchases is exceeded. |
| 28 | `TOTAL_RECEIVE_ALERT_EMAIL` | VARCHAR(255) |  |  | The email addresses to alert when the sum of all receipts committed exceeds the limit set in total_receive_amt. |
| 29 | `TOTAL_RECEIVE_AMT` | DOUBLE | NOT NULL |  | The limit set for notification when the sum value of all receipts is exceeded. |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `PREV_MM_PROJECT_NBR_TRACK_ID` | [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `MM_PROJECT_NBR_TRACKING_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [ADDITIONAL_AMOUNT](ADDITIONAL_AMOUNT.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| [LINE_ITEM](LINE_ITEM.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| [MM_PROJECT_NBR_TRACKING](MM_PROJECT_NBR_TRACKING.md) | `PREV_MM_PROJECT_NBR_TRACK_ID` |
| [MM_TRANS_GL](MM_TRANS_GL.md) | `MM_PROJECT_NBR_TRACKING_ID` |
| [MM_TRANS_LINE](MM_TRANS_LINE.md) | `MM_PROJECT_NBR_TRACKING_ID` |

