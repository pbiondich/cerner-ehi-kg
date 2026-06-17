# DCP_EQUA_COMPONENT

> This table contains each component as it relates to a dcp equation

**Description:** DCP EQUA COMPONENT  
**Table type:** REFERENCE  
**Primary key:** `DCP_COMPONENT_ID`, `DCP_EQUATION_ID`  
**Columns:** 16  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMPONENT_CODE` | VARCHAR(5) |  |  | A code determined by the db tool to identify the componentColumn |
| 2 | `COMPONENT_DESCRIPTION` | VARCHAR(50) |  |  | a description of the componentColumn |
| 3 | `COMPONENT_FLAG` | DOUBLE |  |  | identifies what kind component this isColumn |
| 4 | `COMPONENT_LABEL` | VARCHAR(50) |  |  | a label the user determines that will be used in the calc when displaying the component |
| 5 | `CONSTANT_VALUE` | DOUBLE |  |  | the value of a numeric constantColumn |
| 6 | `CORRESPONDING_EQUATION_ID` | DOUBLE |  |  | a number that uniquely identifies an equationColumn |
| 7 | `DCP_COMPONENT_ID` | DOUBLE | NOT NULL | PK | a number that uniquely identifies the componentColumn |
| 8 | `DCP_EQUATION_ID` | DOUBLE | NOT NULL | PK FK→ | A unique number that identifies an equation.Column |
| 9 | `DUPLICATE_COMPONENT_NAME` | VARCHAR(50) |  |  | Identifies the parent component of a duplicate |
| 10 | `EVENT_CD` | DOUBLE |  |  | a unique identifier to an event cdColumn |
| 11 | `REQUIRED_IND` | DOUBLE |  |  | identifies whether or not this component is required for this equationColumn |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DCP_EQUATION_ID` | [DCP_EQUATION](DCP_EQUATION.md) | `DCP_EQUATION_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DCP_UNIT_MEASURE](DCP_UNIT_MEASURE.md) | `DCP_COMPONENT_ID` |
| [DCP_UNIT_MEASURE](DCP_UNIT_MEASURE.md) | `DCP_EQUATION_ID` |

