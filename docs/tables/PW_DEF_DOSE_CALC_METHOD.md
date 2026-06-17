# PW_DEF_DOSE_CALC_METHOD

> Table used to store the default weight adjustment and CRCL method of a Plan component.

**Description:** Pathway Default Dose Calculator Method  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACILITY_CD` | DOUBLE | NOT NULL |  | Stores the facility code of the facility for which default method is configured. |
| 2 | `METHOD_CD` | DOUBLE | NOT NULL |  | Stores the code value of the default method selected. |
| 3 | `METHOD_MEAN` | VARCHAR(100) | NOT NULL |  | The CDF_MEANING of the method from code set 4016. |
| 4 | `PATHWAY_COMP_ID` | DOUBLE | NOT NULL | FK→ | Identifies the pathway component. Foreign Key from PATHWAY_COMP table. |
| 5 | `PW_DEF_DOSE_CALC_METHOD_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PW_DEF_DOSE_CALC_METHOD table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PATHWAY_COMP_ID` | [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_COMP_ID` |

