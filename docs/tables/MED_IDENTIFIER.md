# MED_IDENTIFIER

> The Med_identifier file stores all pharmacy identifiers for the formulary.

**Description:** Med_Identifier  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `FLEX_SORT_FLAG` | DOUBLE |  |  | Used to sort the flex records so that the most specific records float to the top |
| 3 | `FLEX_TYPE_CD` | DOUBLE | NOT NULL |  | This indicates the type of flex. This field can be 0, if parent_entity_id is 0. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | Points to the Medication_definition table that the identifier is related to. |
| 5 | `MED_DEF_FLEX_ID` | DOUBLE | NOT NULL | FK→ | Points to the Med_def_flex table that identifier is related to. Can never be 0 |
| 6 | `MED_IDENTIFIER_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MED_IDENTIFIER table. |
| 7 | `MED_IDENTIFIER_TYPE_CD` | DOUBLE | NOT NULL |  | The type of identifier |
| 8 | `MED_INGRED_SET_ID` | DOUBLE | NOT NULL | FK→ | Points to the Med_ingredient_set table that identifier is related to. Can be 0 |
| 9 | `MED_PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | med Package type id |
| 10 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | This field can be 0. If it is not zero, this is a manufacturer level identifier. The MED_PRODUCT that the identifier is related to. |
| 11 | `MED_TYPE_FLAG` | DOUBLE |  |  | Indicates the medication type of the item the identifier is related to. |
| 12 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Coded field that will be a location (Facility, Nursing Unit, Ambulatory) or a 0. |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | If the parent_entity_id is filled out, then this will point to the related table. |
| 14 | `PHARMACY_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the Pharmacy Type that owns the identifier. |
| 15 | `PRIMARY_IND` | DOUBLE |  |  | Indicates that this identifier, for a specific identifier type, is primary. |
| 16 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `VALUE` | VARCHAR(200) |  |  | Text string of identifier. This field is required. |
| 23 | `VALUE_KEY` | VARCHAR(200) |  |  | Text string of identifier. This field is required. |
| 24 | `VALUE_KEY_A_NLS` | VARCHAR(800) |  |  | Corresponding Global support field for the associated VALUE_KEY column. |
| 25 | `VALUE_KEY_NLS` | VARCHAR(402) |  |  | Corresponding Global support field for the associated VALUE_KEY column. Replaced by value_key_a_nls. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `MED_DEF_FLEX_ID` | [MED_DEF_FLEX](MED_DEF_FLEX.md) | `MED_DEF_FLEX_ID` |
| `MED_INGRED_SET_ID` | [MED_INGRED_SET](MED_INGRED_SET.md) | `MED_INGRED_SET_ID` |
| `MED_PACKAGE_TYPE_ID` | [MED_PACKAGE_TYPE](MED_PACKAGE_TYPE.md) | `MED_PACKAGE_TYPE_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |

