# PRICE_SCHED_ITEMS

> Associates Bill Items with Price Schedules. Prices the item.

**Description:** Price Schedule Items  
**Table type:** REFERENCE  
**Primary key:** `PRICE_SCHED_ITEMS_ID`  
**Columns:** 30  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLOWABLE` | DOUBLE |  |  | not used |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BILLING_DISCOUNT_PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Billing priority on the bill item for the associated price schedule |
| 8 | `BILL_ITEM_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the bill item table. It is an internal system assigned number. |
| 9 | `CAPITATION_IND` | DOUBLE |  |  | Indicates whether or not the price schedule item is a capitated, meaning that insurance will pay a per member/per month fee instead of a fee for service. |
| 10 | `CHARGE_LEVEL_CD` | DOUBLE | NOT NULL |  | not used.. |
| 11 | `COPAY` | DOUBLE |  |  | not used |
| 12 | `COST_ADJ_AMT` | DOUBLE | NOT NULL |  | The markup or discount amount reflected in the final charge price. |
| 13 | `DEDUCTIBLE` | DOUBLE |  |  | not used |
| 14 | `DETAIL_CHARGE_IND` | DOUBLE |  |  | For a detail (child) bill item, indicates whether a charge should be created. This flag is set by the "charge" check box in the Pricing Tool. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `EXCLUSIVE_IND` | DOUBLE | NOT NULL |  | Determines whether or not the tax amount will show up as a separate line item on the invoice. 0 = it will not show up as a separate line item on the invoice, 1 = it will show up as a separate line item on the invoice. |
| 17 | `INTERVAL_TEMPLATE_CD` | DOUBLE | NOT NULL |  | The code value from 14274 that indicates which interval template to use in determining what price to assign to a charge. A value of 0 indicates to use the price without any interval logic. |
| 18 | `PERCENT_REVENUE` | DOUBLE |  |  | not used |
| 19 | `PRICE` | DOUBLE |  |  | The price to associate with this bill item for this price schedule. |
| 20 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the price_sched table. It is an internal system assigned number. |
| 21 | `PRICE_SCHED_ITEMS_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the price_sched_items table. It is an internal system assigned number. |
| 22 | `REFERRAL_REQ_IND` | DOUBLE |  |  | Indicates whether or not the price schedule item requires a referral |
| 23 | `STATS_ONLY_IND` | DOUBLE |  |  | This allows the user to track statistics at the price schedule level instead of at the bill item level like it currently exists. |
| 24 | `TAX` | DOUBLE | NOT NULL |  | The tax amount for a given price schedule for a given bill item based on a tax percentage. |
| 25 | `UNITS_IND` | DOUBLE |  |  | This indicates whether a price is stored or if units are stored. This was included to accommodate LMS Billing requirements (Canadian). |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILL_ITEM_ID` | [BILL_ITEM](BILL_ITEM.md) | `BILL_ITEM_ID` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [PFT_FEE_SCHED_RELTN](PFT_FEE_SCHED_RELTN.md) | `PRICE_SCHED_ITEMS_ID` |
| [PRICE_SCHED_ITEMS_HIST](PRICE_SCHED_ITEMS_HIST.md) | `PRICE_SCHED_ITEMS_ID` |

