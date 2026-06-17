# CE_MED_ADMIN_IDENT

> Detail table used to store medication identifiers associated with formulary, dispense, or Multum.

**Description:** Clinical Event Medication Administration Identifier  
**Table type:** ACTIVITY  
**Primary key:** `CE_MED_ADMIN_IDENT_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BARCODE_SOURCE_CD` | DOUBLE | NOT NULL |  | The identifier type used to identify the type of medication stored. |
| 2 | `CE_MED_ADMIN_IDENT_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the CE_MED_ADMIN_IDENT table. |
| 3 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense history Id. This is the primary identifier to the dispense_hx table. |
| 4 | `DRUG_IDENT` | VARCHAR(255) |  |  | A generic or universal identifier captured from foreign systems to reflect product information given at administration time. |
| 5 | `INV_FILL_LOCATION_CD` | DOUBLE |  | FK→ | The location that the medication product was acquired from for administration or the inventory location supplying the product used during the administration of the medication.Code Set 220. |
| 6 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The drug formulation. This is the primary identifier to the medication_definition table. |
| 7 | `MED_ADMIN_BARCODE` | VARCHAR(200) | NOT NULL |  | Represents the identifier that matches the product (required). |
| 8 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | Contains the specific manufacturer item identifier. This is the primary identifier to the med_product table. |
| 9 | `PREV_CE_MED_ADMIN_IDENT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the unique ID of the previous version of the current row. |
| 10 | `SCAN_QTY` | DOUBLE | NOT NULL |  | The number of items that were given to make up the dose. (must be greater than zero) |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 16 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the beginning point of when a row in the table is valid. |
| 17 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the end point of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `INV_FILL_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `PREV_CE_MED_ADMIN_IDENT_ID` | [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `CE_MED_ADMIN_IDENT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CE_MED_ADMIN_IDENT](CE_MED_ADMIN_IDENT.md) | `PREV_CE_MED_ADMIN_IDENT_ID` |
| [CE_MED_ADMIN_IDENT_RELTN](CE_MED_ADMIN_IDENT_RELTN.md) | `CE_MED_ADMIN_IDENT_ID` |

