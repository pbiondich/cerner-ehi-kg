# SA_REF_MACRO_MEDICATION

> Contains detail records about medications for a macro, when a line is executed a medication will be added to the anesthesia record. If the dosage, route, and unit cd are populated - an administration record will be added. Based on the # of Macros they have built. Estimate a 2:1 with SA_REF_MACRO. 200

**Description:** SA Reference Macro Medication  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_MACRO_MEDICATION_ID`  
**Columns:** 39  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | This column is now obsolete. Valid data is in table SA_REF_MACRO_MED_ITEM. 8/1/03. Admin Amount |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | This column is now obsolete. Valid data is in table SA_REF_MACRO_MED_ITEM. 8/1/03. The dosage amount that will be used for the medication administration record that is added |
| 7 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | The admin rate code |
| 8 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route_cd that will be used for the medication administration record that is added |
| 9 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site_cd that will be used for the medication administration record that is added |
| 10 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | The admin unit code |
| 11 | `CONCENTRATION` | DOUBLE |  |  | ** OBSOLETE** Concentration NumberThis column will be addition of unit code columns - 6/24/05CAPE 158789 |
| 12 | `CONC_AMOUNT` | DOUBLE | NOT NULL |  | amount field of concentration |
| 13 | `CONC_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount field of concentration |
| 14 | `CONC_DOSAGE` | DOUBLE | NOT NULL |  | dosage field of concentration |
| 15 | `CONC_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage field of concentration |
| 16 | `DILUENT_CONC_VOLUME` | DOUBLE | NOT NULL |  | Diluent volume field for concentration |
| 17 | `DILUENT_ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that identifies the diluent item, FK from item_master |
| 18 | `DIR_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in DIR |
| 19 | `DIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in DIR |
| 20 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit_cd that will be used for the medication administration record that is added |
| 21 | `EXCLUDE_DIL_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude diluent ingredient volume from total concentration volume |
| 22 | `EXCLUDE_MED_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude medication ingredient volume from total concentration volume |
| 23 | `EXECUTE_IND` | DOUBLE |  |  | Indicates whether this record is executed by default. 1=by default, execute this detail record when the macro is executed, the user will have to uncheck the record if they do not want this detail record executed. 0=by default, do not execute this detail record when the macro is executed. This detail record still shows up under the macro, but the user will have to mark this record if they want this record executed. |
| 24 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Item ID from Item master |
| 25 | `MED_ADMIN_TYPE_FLAG` | DOUBLE |  |  | Med Admin Type Flag |
| 26 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The id that identifies the actual pharmacy product item FK from MED_PRODUCT |
| 27 | `PIR_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount in PIR |
| 28 | `PIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in PIR |
| 29 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The macro id that this medication detail belongs to |
| 30 | `SA_REF_MACRO_MEDICATION_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies each macro medication detail record |
| 31 | `TODO_IND` | DOUBLE | NOT NULL |  | Indicates whether the item defaults to be put on the ToDo list when the macro is executed |
| 32 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 33 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 34 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 35 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 36 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 37 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in WBD |
| 38 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in WBD |
| 39 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DILUENT_ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `SA_REF_MACRO_ID` | [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_MACRO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_REF_MACRO_MED_ITEM](SA_REF_MACRO_MED_ITEM.md) | `SA_REF_MACRO_MEDICATION_ID` |

