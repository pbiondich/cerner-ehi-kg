# MM_PROFILE

> Contains the different user profiles used by multiple ProCure applications.

**Description:** MM PROFILE  
**Table type:** REFERENCE  
**Primary key:** `PROFILE_ID`  
**Columns:** 47  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACK_VAR_AMT` | DOUBLE |  |  | The currency amount in which the acknowledged can vary compared to the purchased. |
| 2 | `ACK_VAR_IND` | DOUBLE |  |  | Indicates whether or not to check for this type of variance. |
| 3 | `ACK_VAR_PCT` | DOUBLE |  |  | The percent in which the acknowledged can vary compared to the purchased. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `ALLOW_BACKORDER_IND` | DOUBLE |  |  | Indicates whether or not this profile will allow backorders. |
| 9 | `ALLOW_OVERSHIPMENT_IND` | DOUBLE |  |  | Indicates whether or not this profile will allow overshipments. |
| 10 | `ALLOW_REMAINING_SHELF_LIFE_IND` | DOUBLE | NOT NULL |  | Indicates that the user wants to activate the remaining shelf life functionality. |
| 11 | `AUTO_PAY_IND` | DOUBLE |  |  | Determines whether the option is selected or not in mmprofile.exe. 0 = Auto pay option is not selected for the Invoicing profile, 1 = Auto pay option is selected for the invoicing profile. |
| 12 | `BLANK_INV_DATE_IND` | DOUBLE | NOT NULL |  | Indicates if the invoice date should be blank by default while creating a new invoice. |
| 13 | `BLIND_RECEIPT_IND` | DOUBLE |  |  | Indicates whether or not this profile institutes blind receiving. |
| 14 | `CONTRACT_VAR_AMT` | DOUBLE |  |  | The currency amount in which the contract can vary compared to the invoiced. |
| 15 | `CONTRACT_VAR_IND` | DOUBLE |  |  | Indicates whether or not to check for contract price variance. |
| 16 | `CONTRACT_VAR_PCT` | DOUBLE |  |  | The percent amount in which the contract can vary compared to the invoiced. |
| 17 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 18 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the row was was inserted. |
| 19 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the insert of the row in the table. |
| 20 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 21 | `DEFAULT_FROM_RECEIVING_IND` | DOUBLE |  |  | If true then invoice matching will automatically pull the cost center and subaccount information from the cost center and subaccount defined in transacctmaintenance for a given purchase receipt. |
| 22 | `DESCRIPTION` | VARCHAR(60) |  |  | The description of this profile. |
| 23 | `DISPLAY` | VARCHAR(40) |  |  | The display (short description) for this profile. |
| 24 | `EXCEPTION_EMAIL` | VARCHAR(255) |  |  | Contains the email address defined in mmprofilebuild.exe |
| 25 | `EXCEPTION_PRINTER` | VARCHAR(60) |  |  | Contains the printer name defined in mmprofilebuild |
| 26 | `INV_ADDL_AMT_VAR_AMT` | DOUBLE |  |  | invoice additional amount variable amount |
| 27 | `INV_ADDL_AMT_VAR_IND` | DOUBLE |  |  | determines whether the variance has to calculated for Additional amount0 - Variance will not be calculated for additional amount1 - Variance will be calculated for additional amount |
| 28 | `INV_SAVE_MISMATCH_IND` | DOUBLE | NOT NULL |  | Indicates whether to save the invoice in PAY status if voucher and invoice amounts are not matched. |
| 29 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 30 | `MANUAL_RECEIPT_IND` | DOUBLE |  |  | Indicates whether or not this profile institutes manual receiving. |
| 31 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the organization that the profile is tied too. |
| 32 | `PO_INVOICE_LESS_VAR_AMT` | DOUBLE | NOT NULL |  | Stores the lesser variance limit amount for invoice line amount. |
| 33 | `PO_INVOICE_LESS_VAR_PCT` | DOUBLE | NOT NULL |  | Stores the lesser variance limit percentage for invoice line amount. |
| 34 | `PO_INVOICE_VAR_AMT` | DOUBLE |  |  | PO / Invoice Variance Amount |
| 35 | `PO_INVOICE_VAR_PCT` | DOUBLE |  |  | PO / Invoice Variance Percent |
| 36 | `PO_MAX_LINES` | DOUBLE |  |  | The maximum allowed lines per purchase order. |
| 37 | `PROFILE_ID` | DOUBLE | NOT NULL | PK | Primary key |
| 38 | `PROFILE_TYPE_CD` | DOUBLE | NOT NULL |  | The type of profile. |
| 39 | `RCV_LOC_CD` | DOUBLE | NOT NULL |  | The location at which shipments are received for this profile. |
| 40 | `REMAINING_SHELF_LIFE_PCT` | DOUBLE | NOT NULL |  | The acceptable remaining shelf life for the item under the specific profile. |
| 41 | `UNIT_PRICE_IND` | DOUBLE |  |  | *** OBSOLETE *** |
| 42 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 43 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 44 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 45 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 46 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 47 | `VIEW_PRICE_IND` | DOUBLE |  |  | Used to determine if the user can view the price in the receiving application. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [INVOICE](INVOICE.md) | `INV_PROFILE_ID` |
| [MM_PROFILE_GROUP](MM_PROFILE_GROUP.md) | `PROFILE_ID` |
| [MM_REQ_FILL_ROUTE](MM_REQ_FILL_ROUTE.md) | `PUR_PROFILE_ID` |
| [MM_REQ_FILL_ROUTE](MM_REQ_FILL_ROUTE.md) | `RCV_PROFILE_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `PUR_PROFILE_ID` |
| [PURCHASE_ORDER](PURCHASE_ORDER.md) | `RCV_PROFILE_ID` |
| [VENDOR_SITE](VENDOR_SITE.md) | `RCV_PROFILE_ID` |

