# PATIENT_DISPENSE

> A record of every time a product is dispensed to a patient.

**Description:** Patient Dispense  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BACKDATED_ON_DT_TM` | DATETIME |  |  | The date and time the dispense was backdated on. |
| 6 | `BB_ID_NBR` | VARCHAR(20) |  |  | An optional column that indicates the armband number for the patient as it was entered at the time of dispense. |
| 7 | `CUR_DISPENSE_INTL_UNITS` | DOUBLE |  |  | This column only applies to derivatives, not blood products. It defines the number of international units currently dispensed to the patient on this row. |
| 8 | `CUR_DISPENSE_QTY` | DOUBLE |  |  | This column only applies to derivative products, not blood products. It defines the quantity of this derivative that is currently dispensed to this patient. |
| 9 | `DEVICE_ID` | DOUBLE | NOT NULL | FK→ | The physical location to which this product was dispensed (ex. "Surgery", "ICU") |
| 10 | `DISPENSE_COOLER_ID` | DOUBLE | NOT NULL | FK→ | If the product was placed in a cooler at the time of dispense, this column contains that cooler ID. |
| 11 | `DISPENSE_COOLER_TEXT` | VARCHAR(40) |  |  | If this product was dispensed in a cooler, and that specific cooler had not been defined in the reference database previously, this column contains the free textname or number of the cooler used. |
| 12 | `DISPENSE_COURIER_ID` | DOUBLE | NOT NULL |  | The person who took the product from the blood bank to the patient's location. |
| 13 | `DISPENSE_COURIER_TEXT` | VARCHAR(100) |  |  | A free text entry of the name of the person who took the product from the blood bank to the patient's location. This column is used when the dispense courier has not been defined in the database prior to the dispense transaction taking place. |
| 14 | `DISPENSE_FROM_LOCN_CD` | DOUBLE | NOT NULL |  | The location of the product when it was dispensed. |
| 15 | `DISPENSE_PROV_ID` | DOUBLE | NOT NULL |  | The provider (physician) who ordered this product to be dispensed to this patient. |
| 16 | `DISPENSE_REASON_CD` | DOUBLE | NOT NULL |  | The reason the product was dispensed to this patient. |
| 17 | `DISPENSE_STATUS_FLAG` | DOUBLE |  |  | The current status of this dispense transaction. Defines whether it has resulted in a transfusion, a return of the product to the blood bank, or is still dispensed. |
| 18 | `DISPENSE_TO_LOCN_CD` | DOUBLE | NOT NULL |  | Defines the location to which this product was dispensed (ex. "Surgery", "ICU"). |
| 19 | `DISPENSE_VIS_INSP_CD` | DOUBLE | NOT NULL |  | The outcome of the visual inspection as recorded by the technologist who dispensed the product. |
| 20 | `ORIG_DISPENSE_INTL_UNITS` | DOUBLE |  |  | The number of international units originally dispensed in this transaction. Since some of the batch dispensed could be returned and some transfused, this value could be greater than the number currently dispensed. |
| 21 | `ORIG_DISPENSE_QTY` | DOUBLE |  |  | The quantity of this derivative originally dispensed in this transaction. Since some of the batch dispensed could be returned and some transfused, this value could be greater than the quantity currently dispensed. |
| 22 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 23 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key of this table, from the PRODUCT_EVENT table. |
| 24 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the product table. It is an internal system-assigned number. On this table, it denotes the product dispensed to the patient. |
| 25 | `TAG_VERIFY_FLAG` | DOUBLE |  |  | This field indicates the status of tag verification on dispensed product. 0 - Not configured, 1- Tag verified, 2 - Tag verify overridden |
| 26 | `UNKNOWN_PATIENT_IND` | DOUBLE |  |  | Determines whether the product was dispensed to an unknown patient (as in the case of an emergency). |
| 27 | `UNKNOWN_PATIENT_TEXT` | VARCHAR(50) |  |  | If the product was dispensed to an unknown patient (as in the case of an emergency, where there is no medical record number), it contains free textidentifying the patient's name. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DEVICE_ID` | [BB_INV_DEVICE](BB_INV_DEVICE.md) | `BB_INV_DEVICE_ID` |
| `DISPENSE_COOLER_ID` | [BB_INV_DEVICE](BB_INV_DEVICE.md) | `BB_INV_DEVICE_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |

