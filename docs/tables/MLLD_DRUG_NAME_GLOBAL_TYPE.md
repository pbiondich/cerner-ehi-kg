# MLLD_DRUG_NAME_GLOBAL_TYPE

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DRUG_NAME_GLOBAL_TYPE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABUSE_FLAG` | DOUBLE |  |  | Doping Drug |
| 2 | `DRUG_NAME` | VARCHAR(255) | NOT NULL |  | Identified drug name |
| 3 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Drug synonym ID as defined by external source |
| 4 | `GENERIC_AVAILABLE_FLAG` | DOUBLE |  |  | generic available flag values are: 2 = referent product; 1 = generic product; 0 = all the others products which are not registered on the generic repertory |
| 5 | `GLOBAL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | FK to MLLD_GLOBAL_TYPE |
| 6 | `HOSPITAL_USE_FLAG` | DOUBLE |  |  | Drug limited to hospital |
| 7 | `IS_OBSOLETE` | VARCHAR(1) | NOT NULL |  | Identifies if a drug_name was marked as obsolete. |
| 8 | `NOSWITCH_REASON` | VARCHAR(255) |  |  | Field denotes that a drug can be ordered utilizing the cluster drug_name, but that the same drug should be administered each time. |
| 9 | `NOVOS_REASON` | VARCHAR(255) |  |  | Field is used to denote whether or not a drug is to be ordered utilizing the cluster drug name |
| 10 | `SLEEP_INDUCING_FLAG` | DOUBLE |  |  | Drug inducing sleep |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_SYNONYM_ID` | [MLLD_DRUG_NAME](MLLD_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| `GLOBAL_TYPE_ID` | [MLLD_GLOBAL_TYPE](MLLD_GLOBAL_TYPE.md) | `GLOBAL_TYPE_ID` |

