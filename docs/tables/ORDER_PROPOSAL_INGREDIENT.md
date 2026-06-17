# ORDER_PROPOSAL_INGREDIENT

> The table is used to store ingredients associated with an order proposal. For new order proposals, all ingredients are being added. For proposals that end-state an order, no ingredients will be written. For proposals that alter an order (but do not end state it), ingredients can be added, removed, or modified.

**Description:** Order Proposal Ingredient  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_PROPOSAL_INGREDIENT_ID`  
**Columns:** 34  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BAG_FREQUENCY_CD` | DOUBLE | NOT NULL |  | Codified value to identify the bag frequency of this ingredient's occurrence. |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code from the Order_Catalog table that is associated with this ingredient |
| 3 | `CLINICALLY_SIGNIFICANT_FLAG` | DOUBLE | NOT NULL |  | Determines if the ingredient will be clinically significant to the order. 0 - Does not apply or not set, 1 - Not clinically significant, 2 - Clinically significant |
| 4 | `COMP_SEQUENCE` | DOUBLE | NOT NULL |  | A system assigned number, identifying the order of the ingredient within the proposal. |
| 5 | `CONCENTRATION` | DOUBLE | NOT NULL |  | The amount of the ingredient in a given volume. This will only be valued if there is a normalized rate supplied. |
| 6 | `CONCENTRATION_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure on the ingredient's concentration. |
| 7 | `DAYS_OF_ADMINISTRATION_DISPLAY` | VARCHAR(100) |  |  | The textual display of the days of administration for an order proposal ingredient which had variable dosage amounts. This represents the abbreviated formatting of the days of week which is based on the locale of the user creating the order proposal. |
| 8 | `DOSE_ADJUSTMENT_DISPLAY` | VARCHAR(255) |  |  | The textual display of the dose adjustment for an order proposal ingredient. This includes the adjustment percentage and reason for adjustment. The dose calculator text is paired with this field and needs to be considered usage of this field. |
| 9 | `DOSE_CALCULATOR_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The associated LONG_TEXT information (in XML) captured by the dose calculator that contributes to the dosage calculation |
| 10 | `DOSING_CAPACITY` | DOUBLE |  |  | Represents the total number of potential doses for a given day for variable dosing. For variable dosing, this will always be positive, otherwise it will be 0. |
| 11 | `FREETEXT_DOSE` | VARCHAR(255) |  |  | Free text that can be input concerning a dose. It allows the user to write comments about the dose. |
| 12 | `INCLUDE_IN_TOTAL_VOLUME_FLAG` | DOUBLE | NOT NULL |  | Determines if the ingredient is included in the total volume of an order. Valid flag values are: 0 - Not Set or Not Apply, 1 - Not contribute to total volume, 2 - Contribute to total volume. |
| 13 | `INGREDIENT_ALTER_FLAG` | DOUBLE | NOT NULL |  | For proposals to create an order, this field is set to 1, which indicates this is a new ingredient. For a proposal to alter an order, the flag identifies how this ingredient relates to the order's ingredient that this proposal is for. 0 - Unchanged, 1 - Add, 2 - Modified, 3 - Delete. |
| 14 | `INGREDIENT_DISPLAY_LINE` | VARCHAR(255) |  |  | This is the short description of the ingredient containing information such as dose. |
| 15 | `INGREDIENT_SOURCE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the ingredient was added to the order proposal by a user or by the system. 0 - User, 1 - System Balanced, 2 - System auto product assign |
| 16 | `INGREDIENT_TYPE_FLAG` | DOUBLE |  |  | Identifies the type of ingredient. 0 - Not set, 1 - Medication, 2 - Base, 3 - Additive, 4 - Compound parent, 5 - Compound child |
| 17 | `NORMALIZED_RATE` | DOUBLE | NOT NULL |  | The amount of the ingredient to be administered per time unit or the amount of a medication to be administered per patient weight unit per time unit. |
| 18 | `NORMALIZED_RATE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure of the normalized rate. |
| 19 | `ORDERED_AS_MNEMONIC` | VARCHAR(255) |  |  | Text representing a name by which an ingredient was ordered. |
| 20 | `ORDERED_DOSE` | DOUBLE | NOT NULL |  | The amount of dose that was ordered. |
| 21 | `ORDERED_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the ordered dose. |
| 22 | `ORDER_MNEMONIC` | VARCHAR(255) |  |  | The mnemonic of the order for the ingredients. |
| 23 | `ORDER_PROPOSAL_ID` | DOUBLE | NOT NULL | FK→ | The order proposal ID associated with this ingredient. |
| 24 | `ORDER_PROPOSAL_INGREDIENT_ID` | DOUBLE | NOT NULL | PK | The primary key of this table. It is internally assigned by the system. |
| 25 | `STRENGTH` | DOUBLE |  |  | The strength of this ingredient |
| 26 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on strength of this ingredient. |
| 27 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The id of the order catalog synonym for this ingredient. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `VOLUME` | DOUBLE |  |  | The volume of this ingredient. |
| 34 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Codified unit of measure on strength for this ingredient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `DOSE_CALCULATOR_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_PROPOSAL_ID` | [ORDER_PROPOSAL](ORDER_PROPOSAL.md) | `ORDER_PROPOSAL_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_PROPOSAL_INGRED_DOSE](ORDER_PROPOSAL_INGRED_DOSE.md) | `ORDER_PROPOSAL_INGREDIENT_ID` |
| [ORDER_PROPOSAL_INGRED_HST](ORDER_PROPOSAL_INGRED_HST.md) | `ORDER_PROPOSAL_INGREDIENT_ID` |

