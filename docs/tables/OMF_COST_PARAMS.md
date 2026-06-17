# OMF_COST_PARAMS

> omf_cost_params

**Description:** Stores parameters used by the OMF cost feed.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_FISCAL_DT_NBR` | DOUBLE |  |  | Stores the beginning fiscal date used to store standard costs. |
| 2 | `COST_BASIS_TYPE_CD` | DOUBLE | NOT NULL |  | The type of basis to use for costing (ex. Revenue Code, Cost Center). |
| 3 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier of the organization for which the costing parameters apply. |
| 4 | `SCHEDULE_TYPE_CD` | DOUBLE | NOT NULL |  | The cdm schedule for the bill items that are loaded for the OMF cost feed. |
| 5 | `TOTAL_ONLY_IND` | DOUBLE |  |  | Indicates whether only one total cost will be used for each cost basis value OR all of the cost "buckets" will be used (1=use only one total cost, 0=use cost buckets). |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

