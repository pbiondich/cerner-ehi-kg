# SA_MEDICATION_ADMIN

> Contains records that document the administration of medications in an anesthesia record Based on the number of administrations of a given medication. Estimate 3:1 with SA_MEDICATION. 783,000

**Description:** SA Medication Administration  
**Table type:** ACTIVITY  
**Primary key:** `SA_MEDICATION_ADMIN_ID`  
**Columns:** 64  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | This column is now obsolete. Valid data is in table SA_MED_ADMIN_ITEM. 8/1/03. The amount of the medication administered |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | This column is now obsolete. Valid data is in table SA_MED_ADMIN_ITEM. 8/1/03. The amount of the medication administered |
| 7 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | Rate code |
| 8 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route used for the administration |
| 9 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site that the medication was administered |
| 10 | `ADMIN_START_DT_TM` | DATETIME |  |  | This column is now obsolete. Valid data is in table SA_MED_ADMIN_ITEM. 8/1/03. The date/time the administration was started |
| 11 | `ADMIN_STOP_DT_TM` | DATETIME |  |  | This column is now obsolete. Valid data is in table SA_MED_ADMIN_ITEM. 8/1/03. The date/time the administration was ended if it was continuous |
| 12 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Unit code |
| 13 | `BARCODE_SCAN_TXT` | VARCHAR(100) |  |  | The column will hold the NDC code of the scanned medication. |
| 14 | `BEGIN_BAG_EVENT_ID` | DOUBLE | NOT NULL |  | The event ID for the last begin bag written out by SAAnesthesia (from clinical event) |
| 15 | `CHARGED_IND` | DOUBLE | NOT NULL |  | Indicates whether admin has been charged for from anesthesia |
| 16 | `CONCENTRATION` | DOUBLE |  |  | ** OBSOLETE** ConcentrationThis column is no longer used after adding the various unit code and amount columns. 6/24/05. CAPE 158789 |
| 17 | `CONC_AMOUNT` | DOUBLE | NOT NULL |  | amount field of concentration |
| 18 | `CONC_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount field of concentration |
| 19 | `CONC_DOSAGE` | DOUBLE | NOT NULL |  | dosage field of concentration |
| 20 | `CONC_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage field of concentration |
| 21 | `CONTINUED_NO_BEGIN_BAG_IND` | DOUBLE | NOT NULL |  | Indicates the infused medication was continued from an order which didn't have a begin bag event. |
| 22 | `CONTINUE_OUT_IND` | DOUBLE | NOT NULL |  | An indicator to Continue Medication Admin Orders Out of Anesthesia Application |
| 23 | `DDMO_IND` | DOUBLE | NOT NULL |  | Indicates whether the admin sent through the DDMO server when finalized |
| 24 | `DILUENT_CONC_VOLUME` | DOUBLE | NOT NULL |  | Diluent volume field for concentration |
| 25 | `DIR_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in DIR |
| 26 | `DIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in DIR |
| 27 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the amount of the medication administered |
| 28 | `EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical clinical event row. It is returned from DDMO. It is used to cancel a med order and result when unfinalizing a record.. |
| 29 | `EXCLUDE_DIL_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude diluent ingredient volume from total concentration volume |
| 30 | `EXCLUDE_MED_IN_TOTAL_VOL_IND` | DOUBLE |  |  | Indicator to exclude medication ingredient volume from total concentration volume |
| 31 | `GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | identifier of medication administration's grouper clinical event (CLINICAL_EVENT.EVENT_ID) |
| 32 | `HEIGHT` | DOUBLE |  |  | Height value |
| 33 | `HEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Height Unit Code |
| 34 | `IBUS_RESULT_IDENT` | VARCHAR(50) |  |  | The key used to identify individual medication results received from the ibus |
| 35 | `IO_EVENT_ID` | DOUBLE | NOT NULL |  | identifier of medication administration's intake result clinical event (CLINICAL_EVENT.EVENT_ID) |
| 36 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long_text record that contains the comment for the administration |
| 37 | `MED_ADMIN_TYPE_FLAG` | DOUBLE |  |  | Med Admin Type Flag 1 = FLUID_ADMIN_TYPE BOLUS; 2 = FLUID_ADMIN_TYPE INFUSION |
| 38 | `MED_ORDER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of medication order. An example would be dialysis, IV, irrigation, etc. |
| 39 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The column will hold the product id of the scanned medication. |
| 40 | `ORDERED_IND` | DOUBLE | NOT NULL |  | Indicates whether the admin was documented against an existing order or is an ad hoc admin |
| 41 | `ORDER_ID` | DOUBLE | NOT NULL |  | Order that the admin is associated to |
| 42 | `ORDER_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT record that contains the comment for the order |
| 43 | `PIR_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for amount in PIR |
| 44 | `PIR_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in PIR |
| 45 | `PREVIOUS_MED_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | The id to the admin record before the record was changed. If 0, this is the original unchanged record |
| 46 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who documented the administration, if 0, added by a macro |
| 47 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | Identifier of the Result Set the Medication Administrations intake belongs to. From CE_RESULT_SET_LINK. |
| 48 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | Ties to the macro that added the admin to the anesthesia record, if 0, added by user |
| 49 | `SA_MEDICATION_ADMIN_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the medication administration record |
| 50 | `SA_MEDICATION_ID` | DOUBLE | NOT NULL | FK→ | The SA_MEDICATION record id that this administration record is documenting |
| 51 | `SA_REF_DILUENT_ID` | DOUBLE | NOT NULL | FK→ | Unique ID of medication administrations Diluent Item |
| 52 | `SENT_DT_TM` | DATETIME |  |  | Date/Time when administratin was sent to clinical event |
| 53 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | Task that the admin is associated to |
| 54 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Parent Order that admin is documented against |
| 55 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 56 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 57 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 58 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | unit for dosage in WBD |
| 61 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | unit for time in WBD |
| 62 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | unit for weight in WBD |
| 63 | `WEIGHT` | DOUBLE |  |  | Weight Value |
| 64 | `WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit code for Weight |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `ORDER_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREVIOUS_MED_ADMIN_ID` | [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `SA_MEDICATION_ADMIN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `SA_MEDICATION_ID` | [SA_MEDICATION](SA_MEDICATION.md) | `SA_MEDICATION_ID` |
| `SA_REF_DILUENT_ID` | [SA_REF_DILUENT](SA_REF_DILUENT.md) | `SA_REF_DILUENT_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |
| `TEMPLATE_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [SA_MEDICATION_ADMIN](SA_MEDICATION_ADMIN.md) | `PREVIOUS_MED_ADMIN_ID` |
| [SA_MED_ADMIN_ITEM](SA_MED_ADMIN_ITEM.md) | `SA_MEDICATION_ADMIN_ID` |

