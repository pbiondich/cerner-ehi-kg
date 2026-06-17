# ORDER_INGREDIENT

> Table is used to hold all the ingredients to a pharmay order.

**Description:** Table is used to hold all the ingredients to a pharmacy order.  
**Table type:** ACTIVITY  
**Primary key:** `ACTION_SEQUENCE`, `COMP_SEQUENCE`, `ORDER_ID`  
**Columns:** 40  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | PK | The sequence number of the action that was performed for this ingredient. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the coded value for the order catalog code. |
| 3 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the catalog type that the order catalog should be assigned to . |
| 4 | `CLINICALLY_SIGNIFICANT_FLAG` | DOUBLE | NOT NULL |  | Determines if the ingredient is clinically significant to the order |
| 5 | `COMP_SEQUENCE` | DOUBLE | NOT NULL | PK | Defines the sequence of components of ingredients. |
| 6 | `CONCENTRATION` | DOUBLE | NOT NULL |  | The amount of the ingredient in a given volume. |
| 7 | `CONCENTRATION_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure on the ingredient's concentration. |
| 8 | `DAYS_OF_ADMINISTRATION_DISPLAY` | VARCHAR(100) |  |  | The textual display of the days of administration for an order ingredient which had variable dosage amounts. This represents the abbreviated formatting of the days of week which is based on the locale of the user performing the order action. |
| 9 | `DOSE_ADJUSTMENT_DISPLAY` | VARCHAR(255) |  |  | The textual display of the dose adjustment for an order ingredient. This includes the adjustment percentage and reason for adjustment. The dose calculator text is paired with this field and needs to be considered for usage of this field. |
| 10 | `DOSE_CALCULATOR_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The associated LONG_TEXT information (in XML) captured by Dose Calculator that contributes to the dosage calculation at ingredient level. |
| 11 | `DOSE_QUANTITY` | DOUBLE |  |  | The Dose Quantity -probably only used for an interface |
| 12 | `DOSE_QUANTITY_UNIT` | DOUBLE |  |  | The dose quantity unit -probably used only for an interface |
| 13 | `DOSING_CAPACITY` | DOUBLE | NOT NULL |  | Represents the total number of potential doses for a given day which were available during ordering for a variable dose order. For variable dose orders, this will always be populated with a positive value and for non-variable dose orders, this will be 0. |
| 14 | `FREETEXT_DOSE` | VARCHAR(100) |  |  | Free text that can be input concerning a dose. Allows the user to write comments about the dose. |
| 15 | `FREQ_CD` | DOUBLE | NOT NULL |  | Code to identify the frequency of the occurrence of this ingredient. |
| 16 | `HNA_ORDER_MNEMONIC` | VARCHAR(100) |  |  | This is the primary_mnemonic from the order_catalog. (The generic name) |
| 17 | `INCLUDE_IN_TOTAL_VOLUME_FLAG` | DOUBLE | NOT NULL |  | Determines if the ingredient is included in the total volume of an order |
| 18 | `INGREDIENT_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the ingredient was added to the ORDER by a USER, or by the SYSTEM to satisfy an order requirement or as part of an auto assign process. |
| 19 | `INGREDIENT_TYPE_FLAG` | DOUBLE |  |  | This shows what type of ingredient it is. |
| 20 | `IV_SEQ` | DOUBLE |  |  | The IV sequence for this ingredient. |
| 21 | `NORMALIZED_RATE` | DOUBLE | NOT NULL |  | The amount of the ingredient to be administered per time unit or the amount of a medication to be administered per patient weight unit per time unit. |
| 22 | `NORMALIZED_RATE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure of the normalized rate. |
| 23 | `ORDERED_AS_MNEMONIC` | VARCHAR(100) |  |  | Text representing the name by which an ingredient was ordered. |
| 24 | `ORDERED_AS_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The id of the order catalog synonym for the orderable for this ingredient when it's originally ordered. |
| 25 | `ORDERED_DOSE` | DOUBLE | NOT NULL |  | The amount of the dose that was ordered. |
| 26 | `ORDERED_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure on the ordered dose. |
| 27 | `ORDER_DETAIL_DISPLAY_LINE` | VARCHAR(255) |  |  | The display line of order details for this order. |
| 28 | `ORDER_ID` | DOUBLE | NOT NULL | PK FK→ | The order id for the order for this ingredient. Foreign Key to Order table. |
| 29 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | The mnemonic of the order for these ingredients. |
| 30 | `STRENGTH` | DOUBLE |  |  | The strength of this ingredient. |
| 31 | `STRENGTH_UNIT` | DOUBLE |  |  | The unit of measure for the strength of this ingredient. |
| 32 | `SUPPLIED_AS_MNEMONIC` | VARCHAR(100) |  |  | Supplied As this Mnemonic |
| 33 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The id of the order catalog synonym for the orderable for this ingredient. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `VOLUME` | DOUBLE |  |  | The volume of this ingredient. |
| 40 | `VOLUME_UNIT` | DOUBLE |  |  | The units of measure for the volume for this ingredient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOSE_CALCULATOR_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDERED_AS_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [ORDER_INGREDIENT_DOSE](ORDER_INGREDIENT_DOSE.md) | `ACTION_SEQUENCE` |
| [ORDER_INGREDIENT_DOSE](ORDER_INGREDIENT_DOSE.md) | `COMP_SEQUENCE` |
| [ORDER_INGREDIENT_DOSE](ORDER_INGREDIENT_DOSE.md) | `ORDER_ID` |

