# ORDER_INGREDIENT_DOSE

> Store the dosing information for an order ingredient when the dose ma vary per administration.

**Description:** Order Ingredient Dose  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence of the related order action. |
| 2 | `COMP_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The sequence of the related order ingredient component. |
| 3 | `DOSE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the dose of the related order ingredient component. This value will be unique per order action that an ingredient is associated to. For variable dose ingredients, this dose sequence will resemble a dose's position in regards of a static dose capacity (i.e. third dose of four doses). |
| 4 | `ORDERED_DOSE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Flag that indicates the type of dosing (strength vs. volume) that the ordered dose represents. Valid values: 1 - Ordered dose was entered as a strength dose, 2 - Ordered dose was entered as a volume dose. |
| 5 | `ORDERED_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The codified value of the unit of measure associated to the ordered dose. This value will exist if the ordered dose value exists. |
| 6 | `ORDERED_DOSE_VALUE` | DOUBLE | NOT NULL |  | The value of the ordered dose for the given order ingredient dose instance. |
| 7 | `ORDERED_DOSE_VALUE_DISPLAY` | VARCHAR(100) |  |  | The textual display of the ordered dose value for the given order ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order action. If the ordered dose exists, this display value will exist and should be used for any display purposes. |
| 8 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the related order.This is the ORDER_ID value from the PK of ORDER_INGREDIENT (master parent is ORDERS) |
| 9 | `ORDER_INGREDIENT_DOSE_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 10 | `SCHEDULE_SEQUENCE` | DOUBLE | NOT NULL |  | The sequence of the related frequency schedule which this order ingredient dose instance represents. This sequence will always be populated for variable dosing (determined by dosing_method_flag of ORDERS table). |
| 11 | `STRENGTH_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The codified value of the unit of measure associated to the strength dose for the given order ingredient dose instance. This value will exist if the strength dose value exists. |
| 12 | `STRENGTH_DOSE_VALUE` | DOUBLE | NOT NULL |  | The value of the volume dose for the given order ingredient dose instance. |
| 13 | `STRENGTH_DOSE_VALUE_DISPLAY` | VARCHAR(100) |  |  | The textual display of the strength dose value for the given order ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order action. If the strength dose exists, this display value will exist and should be used for any display purposes. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VOLUME_DOSE_UNIT_CD` | DOUBLE | NOT NULL |  | The codified value of the unit of measure associated to the volume dose for the given order ingredient dose instance. This value will exist if the volume dose value exists. |
| 20 | `VOLUME_DOSE_VALUE` | DOUBLE | NOT NULL |  | The value of the volume dose for the given order ingredient dose instance. |
| 21 | `VOLUME_DOSE_VALUE_DISPLAY` | VARCHAR(100) |  |  | The textual display of the volume dose value for the given order ingredient dose instance. This represents the numeric display formatting which relates to the locale of the user performing the order action. If the volume dose exists, this display value will exist and should be used for any display purposes. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `ACTION_SEQUENCE` |
| `COMP_SEQUENCE` | [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `COMP_SEQUENCE` |
| `ORDER_ID` | [ORDER_INGREDIENT](ORDER_INGREDIENT.md) | `ORDER_ID` |

