# PFT_UNIFIED_BILLING_RELTN

> Used to establish links between institutional and professional charge groups for specific payers when a payer requires that all charges be billed on an institutional claim. Specifically it will relate an institutional bo_hp_reltn row to a professional bo_hp_reltn row. An institutional row can have 0 to many professional rows.

**Description:** ProFit Unified Billing Reltn  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DIRECTION_FLAG` | DOUBLE | NOT NULL |  | Indicates the direction the balance association will happen. 1 - Professional -> Institutional2 - Institutional -> Professional |
| 3 | `INST_BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies an institutional benefit order health plan |
| 4 | `PFT_UNIFIED_BILLING_RELTN_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a relationship between an instirutional benefit order health plan and a professional bennefit order health plan. |
| 5 | `PROF_BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a professional benefit order health plan |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INST_BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `PROF_BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |

