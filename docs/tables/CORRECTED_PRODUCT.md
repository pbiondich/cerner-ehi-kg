# CORRECTED_PRODUCT

> All corrections that have been made on a blood bank product.

**Description:** Corrected Product  
**Table type:** ACTIVITY  
**Primary key:** `CORRECTION_ID`  
**Columns:** 66  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABO_CD` | DOUBLE | NOT NULL |  | If the product's ABO group was corrected, then this column will contain the product's original ABO group before it was corrected. |
| 2 | `ALTERNATE_NBR` | VARCHAR(20) |  |  | If the product's alternate number was corrected, then this column will contain the product's original alternate number before it was corrected. |
| 3 | `AUTOCLAVE_IND` | DOUBLE |  |  | If the product's autoclave indicator was corrected, then this column will contain the product's original autoclave indicator before it was corrected. |
| 4 | `BARCODE_NBR` | CHAR(20) |  |  | Defines the original value of the "raw" barcoded version of the product number before it was corrected to a different value. The barcode number (ex. "5012345") is NOT the number with the alpha translation value (ex. "G12345") in it. |
| 5 | `CORRECTION_FLAG` | DOUBLE |  |  | This flag delineates the correction type further. It is currently only used to define types of pooled product changes. |
| 6 | `CORRECTION_ID` | DOUBLE | NOT NULL | PK | The primary key to this table. An internal system-assigned number that makes each row unique. |
| 7 | `CORRECTION_NOTE` | VARCHAR(255) |  |  | A free text entry for the user to make comments regarding the correction made. |
| 8 | `CORRECTION_REASON_CD` | DOUBLE | NOT NULL |  | The reason the product had to be corrected. |
| 9 | `CORRECTION_TYPE_CD` | DOUBLE | NOT NULL |  | The type of correction that took place with this product. These correction types are pre-defined by Cerner. Examples are: demographic changes, emergency dispense correction, etc. |
| 10 | `CORR_DISP_PROD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related corrected dispense product order. |
| 11 | `CUR_AVAIL_QTY` | DOUBLE |  |  | Only applicable to derivative products. The available quantity before it was corrected. |
| 12 | `CUR_INTL_UNITS` | DOUBLE |  |  | Only applicable to derivative products. The number of international units before it was corected. |
| 13 | `CUR_INV_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the current inventory area where the product resided, prior to it being corrected. This inventory area is any area that keeps blood products or derivatives in an inventory, from which the products are dispensed. This means that the it could be the main blood bank, or a surgical area or emergency room that stocks blood for use in surgery. |
| 14 | `CUR_OWNER_AREA_CD` | DOUBLE | NOT NULL |  | Identifies the code value for the current blood bank owner area where the product resides. This owner area is a fully-functioning blood bank that is responsible for the blood received or drawn there. A blood bank owner area can have several inventory areas within it. An example of an owner area would be "General Hospital North", with its inventory areas being "Main BB - GH North", "Surgery - GH North", and "ER - GH North". |
| 15 | `DESTRUCTION_METHOD_CD` | DOUBLE | NOT NULL |  | If the product's destruction method was corrected, then this column will contain the product's original destruction method before it was corrected. |
| 16 | `DESTRUCTION_ORG_ID` | DOUBLE | NOT NULL | FK→ | If the product's destruction organization was corrected, then this column will contain the product's original destruction organization before it was corrected. |
| 17 | `DESTRUCTION_ORG_ID_FLAG` | DOUBLE | NOT NULL |  | This column value indicates whether the value of 'destruction_org_id' column has changed or not. |
| 18 | `DISEASE_CD` | DOUBLE | NOT NULL |  | If the disease was corrected, then this column will store the unique identifier of the disease associated with the product before it was corrected. |
| 19 | `DONATED_BY_RELATIVE_IND` | DOUBLE |  |  | Applies to a person associated to a directed product indicating whether the product was donated by a relative, before it was corrected. |
| 20 | `DONATION_TYPE_CD` | DOUBLE | NOT NULL |  | If the donation type was corrected, then this column will store the unique identifier of the donation type associated with the product before it was corrected. |
| 21 | `DRAWN_DT_TM` | DATETIME |  |  | Original Drawn Date/Time of product prior to correction of Drawn Date/Time |
| 22 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 23 | `EVENT_DT_TM` | DATETIME |  |  | If the product's event date/time was corrected, then this column will contain the product's original event date/time before it was corrected. |
| 24 | `EXPECTED_USAGE_DT_TM` | DATETIME |  |  | The expected usage date and time that was entered for the autologous or directed product, before it was corrected. |
| 25 | `EXPIRE_DT_TM` | DATETIME |  |  | If the product's expire date/time was corrected, then this column will contain the product's original expire date/time before it was corrected. |
| 26 | `FLAG_CHARS` | CHAR(2) |  |  | This column hols the flag characters of an ISBT-128 donation number |
| 27 | `INTENDED_USE_PRINT_PARM_TXT` | VARCHAR(1) |  |  | This information is copied from the field named the same on the PRODUCT table. |
| 28 | `MANIFEST_NBR` | VARCHAR(50) |  |  | If the product's manifest number was corrected, then this column will contain the product's original manifest number before it was corrected. |
| 29 | `MANUFACTURER_ID` | DOUBLE | NOT NULL | FK→ | Only applicable to derivative products. The original manufacturer of this product before it was corrected. |
| 30 | `ORIG_DISP_PROD_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the original dispense product order. |
| 31 | `ORIG_DISP_PROV_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the original provider (physician) who ordered the product to be dispensed. |
| 32 | `ORIG_LOT_NBR` | VARCHAR(25) | NOT NULL |  | This column contains the product's original lot number before any corrections were made. |
| 33 | `ORIG_UPDT_APPLCTX` | DOUBLE |  |  | The product's original application context number from the record info block, as it existed before it was corrected. |
| 34 | `ORIG_UPDT_CNT` | DOUBLE |  |  | The product's original update count, as it existed before it was corrected. |
| 35 | `ORIG_UPDT_DT_TM` | DATETIME |  |  | The product's original update date and time, as it existed before it was corrected. |
| 36 | `ORIG_UPDT_ID` | DOUBLE | NOT NULL | FK→ | The product's original update ID, as it existed before it was corrected. |
| 37 | `ORIG_UPDT_TASK` | DOUBLE |  |  | The product's original update task, as it existed before it was corrected. |
| 38 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 39 | `POOLED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | If this product had previously been a component of a pooled product, and was removed from that pool, this number is the product_id of that pooled product. |
| 40 | `PRODUCT_CAT_CD` | DOUBLE | NOT NULL |  | If the product type was corrected, then this column will contain the product's original category before it was corrected. |
| 41 | `PRODUCT_CD` | DOUBLE | NOT NULL |  | If the product type was corrected, then this column will contain the product's original type before it was corrected. |
| 42 | `PRODUCT_CLASS_CD` | DOUBLE | NOT NULL |  | If the product type was corrected, then this column will contain the product's original class before it was corrected. |
| 43 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT_EVENT table. An internal system-assigned number. On this table, if the product was corrected for emergency dispense information or changing the final disposition state, then this column will contain the product event ID of that dispense or disposition transaction that was corrected. |
| 44 | `PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The primary key to the PRODUCT table. An internal system-assigned number. On this table, it identifies the product that was corrected. |
| 45 | `PRODUCT_NBR` | VARCHAR(20) |  |  | If the product number from the label on the bag was corrected, then this column will contain the product's original number before it was corrected. |
| 46 | `PRODUCT_SUB_NBR` | CHAR(5) |  |  | If the product's sub number was corrected, then this column will contain the product's original sub number before it was corrected. |
| 47 | `PRODUCT_TYPE_BARCODE` | VARCHAR(22) |  |  | This is the barcode value that was entered in BBReceiveProducts or corrected in Correct Inventory. |
| 48 | `REASON_CD` | DOUBLE | NOT NULL |  | If the product's final disposition state was corrected, then this column will contain the product's original final disposition reason before it was corrected. |
| 49 | `RECV_DT_TM` | DATETIME |  |  | If the product's receipt date and time was corrected, then this column will contain the product's original receipt date and time before it was corrected. |
| 50 | `RELATED_CORRECTION_ID` | DOUBLE | NOT NULL | FK→ | The correction ID of another row on the Corrected_Product table that is related to this row. This column is currently only used to tie the correction on a component of the pool to a correction of the pooled product. This allows the system to know the pooled product to which a component was added, or the pooled product from which a component was removed. |
| 51 | `RH_CD` | DOUBLE | NOT NULL |  | If the product's Rh type was corrected, then this column will contain the product's original Rh type before it was corrected. |
| 52 | `SEGMENT_NBR` | VARCHAR(25) |  |  | If the product's segment number was corrected, then this column will contain the product's original segment number before it was corrected. |
| 53 | `SERIAL_NUMBER_TXT` | VARCHAR(22) |  |  | Contains GS1 serial number for derivative products when applicable. |
| 54 | `SHIP_COND_CD` | DOUBLE | NOT NULL |  | If the shipping condition was corrected, then this field will contain the product shipping condition prior to the correction. |
| 55 | `SUPPLIER_ID` | DOUBLE | NOT NULL | FK→ | If the product's supplier ID was corrected, then this column will contain the product's original supplier ID before it was corrected. |
| 56 | `SUPPLIER_PREFIX` | CHAR(5) |  |  | Defines the original value of the originating supplier prefix before it was corrected to a different value. |
| 57 | `UNITS_PER_VIAL_CNT` | DOUBLE | NOT NULL |  | This value is only applicable to derivative products. The units per vial before the product was corrected. |
| 58 | `UNIT_MEAS_CD` | DOUBLE | NOT NULL |  | If the product's unit of measure was corrected, then this column will contain the product's original unit of measure before it was corrected. |
| 59 | `UNKNOWN_PATIENT_TEXT` | VARCHAR(50) |  |  | If the product was corrected for emergency dispense information, then this column will contain the unknown patient text of that dispense transaction as it existed before it was corrected. |
| 60 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 64 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 65 | `VIS_INSP_CD` | DOUBLE | NOT NULL |  | If the product's visual inspection was corrected, then this field will contain the visual inspection prior to the correction |
| 66 | `VOLUME` | DOUBLE |  |  | If the product's volume was corrected, then this column will contain the product's original volume as it existed before it was corrected. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CORR_DISP_PROD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `DESTRUCTION_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MANUFACTURER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `ORIG_DISP_PROD_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORIG_DISP_PROV_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_UPDT_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `POOLED_PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `PRODUCT_EVENT_ID` | [PRODUCT_EVENT](PRODUCT_EVENT.md) | `PRODUCT_EVENT_ID` |
| `PRODUCT_ID` | [PRODUCT](PRODUCT.md) | `PRODUCT_ID` |
| `RELATED_CORRECTION_ID` | [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `CORRECTION_ID` |
| `SUPPLIER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CORRECTED_PRODUCT](CORRECTED_PRODUCT.md) | `RELATED_CORRECTION_ID` |
| [CORRECTED_SPECIAL_TESTS](CORRECTED_SPECIAL_TESTS.md) | `CORRECTION_ID` |

