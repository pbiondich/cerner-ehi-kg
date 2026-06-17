# SA_TODO_MEDICATION

> Surginet Anesthesia To Do Medication

**Description:** SA To Do Medication  
**Table type:** ACTIVITY  
**Primary key:** `SA_TODO_MEDICATION_ID`  
**Columns:** 44  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | The unit of measure for the rate the medication to be given |
| 6 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route the medication is to be given |
| 7 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site the medication is to be given |
| 8 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | The amount unit code |
| 9 | `COMPLETE_DT_TM` | DATETIME |  |  | The date/time the todo item was completed |
| 10 | `COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates whether the todo item has been completed |
| 11 | `CONCENTRATION` | DOUBLE |  |  | ** OBSOLETE** The concentration of the medicationThis column will no longer be used after addition of the various unit code and amount columns. 6/24/05. CAPE 158789 |
| 12 | `CONC_AMOUNT` | DOUBLE | NOT NULL |  | amount field of concentration |
| 13 | `CONC_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount field of concentration |
| 14 | `CONC_DOSAGE` | DOUBLE | NOT NULL |  | dosage field of concentration |
| 15 | `CONC_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage field of concentration |
| 16 | `DILUENT_CONC_VOLUME` | DOUBLE | NOT NULL |  | Diluent volume field for concentration |
| 17 | `DILUENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that identifies the diluent item, FK from ITEM_MASTER |
| 18 | `DIR_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in DIR |
| 19 | `DIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in DIR |
| 20 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the dose of the medication to be given |
| 21 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter which the order is associated with. |
| 22 | `EXCLUDE_DIL_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude diluent ingredient volume from total concentration volume |
| 23 | `EXCLUDE_MED_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude medication ingredient volume from total concentration volume |
| 24 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item id for the medication |
| 25 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text identifier |
| 26 | `MED_ADMIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of admin (bolus or infusion) this item is |
| 27 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of medication order. An example would be dialysis, IV, irrigation, etc. |
| 28 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The med product id for the medication |
| 29 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order that the Admin is associated to |
| 30 | `PIR_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount in PIR |
| 31 | `PIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in PIR |
| 32 | `PREV_TODO_MEDICATION_ID` | DOUBLE | NOT NULL | FK→ | The previous version of the todo medication item |
| 33 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The provider who added the item to the todo list. |
| 34 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The instance of a macro that added the item to the todo list. |
| 35 | `SA_TODO_LIST_ID` | DOUBLE | NOT NULL | FK→ | The ToDo list record this item belongs to |
| 36 | `SA_TODO_MEDICATION_ID` | DOUBLE | NOT NULL | PK | Unique Identifier for this record |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 42 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in WBD |
| 43 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in WBD |
| 44 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DILUENT_ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PREV_TODO_MEDICATION_ID` | [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `SA_TODO_MEDICATION_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_TODO_LIST_ID` | [SA_TODO_LIST](SA_TODO_LIST.md) | `SA_TODO_LIST_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_TODO_MEDICATION](SA_TODO_MEDICATION.md) | `PREV_TODO_MEDICATION_ID` |
| [SA_TODO_MED_ITEM](SA_TODO_MED_ITEM.md) | `SA_TODO_MEDICATION_ID` |

