# SA_REF_MACRO_FLUID

> Contains detail records about fluids for a macro, when a line is executed a fluid will be added to the anesthesia record. If the dosage, site and unit cd are populated - an administration record will be added. Based on the # of Macros they have built. Estimate a 1:1 with SA_REF_MACRO. 100

**Description:** SA Ref Macro Fluid  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_MACRO_FLUID_ID`  
**Columns:** 32  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | The dosage amount that will be used for the fluid administration record that is added |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | This column is not being used. OBSOLETE |
| 7 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | The unit_cd that will be used for the fluid administration record that is added |
| 8 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | Admin Route Code |
| 9 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site_cd that will be used for the fluid administration record that is added |
| 10 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Amount Unit Code |
| 11 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | This column is not being used. OBSOLETE |
| 12 | `EVENT_CD` | DOUBLE | NOT NULL |  | The event code |
| 13 | `EXECUTE_IND` | DOUBLE | NOT NULL |  | Execute Indicator |
| 14 | `FLUID_ADMIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Fluid Admin Type Flag 0 not defined; 1 Bolus; 2 Infusion |
| 15 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | ITEM ID FROM ITEM MASTER |
| 16 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Medical Product ID. FK from Med_Product |
| 17 | `OUT_IND` | DOUBLE |  |  | This column is not being used. OBSOLETE |
| 18 | `SA_REF_MACRO_FLUID_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies each macro fluid detail record |
| 19 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | FK→ | The macro id that this fluid detail belongs to |
| 20 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Task Assay code |
| 21 | `TODO_IND` | DOUBLE | NOT NULL |  | Indicates whether the item defaults to be put on the ToDo list when the macro is executed |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `VOLUME_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of volume |
| 28 | `VOLUME_RATE_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of Volume Rate |
| 29 | `VOLUME_RATE_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time field of Volume Rate |
| 30 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in WBD |
| 31 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in WBD |
| 32 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for weight in WBD |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_MASTER](ITEM_MASTER.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `SA_REF_MACRO_ID` | [SA_REF_MACRO](SA_REF_MACRO.md) | `SA_REF_MACRO_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SA_REF_MACRO_FLUID_ITEM](SA_REF_MACRO_FLUID_ITEM.md) | `SA_REF_MACRO_FLUID_ID` |

