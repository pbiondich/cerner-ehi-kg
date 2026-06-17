# DCP_UNIT_MEASURE

> This table contains the unit of measures for each component in an equation

**Description:** DCP UNIT MEASURE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DCP_COMPONENT_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a single component in an equation.Column |
| 2 | `DCP_EQUATION_ID` | DOUBLE | NOT NULL | FK→ | This is the unique identifier for the parent equationColumn |
| 3 | `DEFAULT_IND` | DOUBLE |  |  | This indicator is used to determine whether a not this unit of measure is the defaulted unit of measure |
| 4 | `EQUATION_DEPENDENT_UNIT_IND` | DOUBLE |  |  | This indicator is used to determine which unit of measure the equation depends on for this component |
| 5 | `UNIT_MEASURE_CD` | DOUBLE | NOT NULL |  | This is the unique identifier for the unit of measureColumn |
| 6 | `UNIT_MEASURE_MEANING` | VARCHAR(12) |  |  | This contains the cdf meaning of the chosen unit of measure |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_COMPONENT_ID` | [DCP_EQUA_COMPONENT](DCP_EQUA_COMPONENT.md) | `DCP_COMPONENT_ID` |
| `DCP_EQUATION_ID` | [DCP_EQUA_COMPONENT](DCP_EQUA_COMPONENT.md) | `DCP_EQUATION_ID` |

