# ORDER_PROPOSAL_INGRED_DOSE

> Stores the dosing information for an order proposal ingredient when the dose may vary per administration.

**Description:** Order Proposal Ingredient Dose  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOSE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the dose of the related order proposal ingredient component. For variable dose ingredients, this dose sequence will resemble a dose's position in regards of a static capacity (i.e. third dose of four doses). |
| 2 | `ORDERED_DOSE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag that indicates the type of dosing the ordered dose represents. Valid values: 1 - Ordered dose was entered as a strength dose, 2 - Ordered dose was entered as a volume dose. |
| 3 | `ORDERED_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The codified value of the unit of measure associated to the ordered dose. This value will exist if the ordered dose value exists. |
| 4 | `ORDERED_DOSE_VALUE` | DOUBLE | NOT NULL |  | The value of the ordered dose for the given order ingredient dose instance. |
| 5 | `ORDERED_DOSE_VALUE_DISPLAY` | VARCHAR(100) | NOT NULL |  | The textual display of the ordered dose value for the given order proposal ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order proposal action. If the ordered dose exists, this display value will exist and should be used for any display purposes. |
| 6 | `ORDER_PROPOSAL_INGREDIENT_ID` | DOUBLE | NOT NULL | FK→ | The ID of the related order_proposal_ingredient. |
| 7 | `ORDER_PROPOSAL_INGRED_DOSE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORDER_PROPOSAL_INGRED_DOSE table. |
| 8 | `SCHEDULE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the related frequency schedule which this order proposal ingredient dose instance represents. This sequence will always be populated for variable dosing (determined by dosing_method_flag of ORDER_PROPOSAL table). |
| 9 | `STRENGTH_DOSE_UNIT_CD` | DOUBLE |  |  | The codified value of the unit of measure associated to the strength dose for the given order proposal ingredient dose instance. This value will exist if the strength dose value exists. |
| 10 | `STRENGTH_DOSE_VALUE` | DOUBLE |  |  | The value of the strength dose for the given order proposal ingredient dose instance. |
| 11 | `STRENGTH_DOSE_VALUE_DISPLAY` | VARCHAR(100) |  |  | The textual display of the strength dose value for the given order proposal ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order proposal action. If the strength dose exists, this display value will exist and should be used for any display purposes. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `VOLUME_DOSE_UNIT_CD` | DOUBLE |  |  | The codified value of the unit of measure associated to the volume dose for the order proposal ingredient dose instance. This value will exist if the volume dose value exists. |
| 18 | `VOLUME_DOSE_VALUE` | DOUBLE |  |  | The value of the volume dose for the given order proposal ingredient dose instance. |
| 19 | `VOLUME_DOSE_VALUE_DISPLAY` | VARCHAR(100) |  |  | The textual display of the volume dose value for the given order proposal ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order proposal action. If the volume dose exists, this display value will exist and should be used for any display purposes. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_PROPOSAL_INGREDIENT_ID` | [ORDER_PROPOSAL_INGREDIENT](ORDER_PROPOSAL_INGREDIENT.md) | `ORDER_PROPOSAL_INGREDIENT_ID` |

