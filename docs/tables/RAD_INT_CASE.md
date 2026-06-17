# RAD_INT_CASE

> The Rad_Int_Case table identifies the groups in which interesting cases will be collected.

**Description:** Rad Interesting Case  
**Table type:** REFERENCE  
**Primary key:** `INT_CASE_ID`  
**Columns:** 12  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `INT_CASE_DESC` | VARCHAR(50) |  |  | The Int_Case_Desc is the description of the interesting case. |
| 3 | `INT_CASE_ID` | DOUBLE | NOT NULL | PK | The Int_Case_Id uniquely identifies a row in the Rad_Int_Case table. It serves no other purpose other than to uniquely identify the row. |
| 4 | `PARENT_INT_CASE_ID` | DOUBLE | NOT NULL | FK→ | Parent subclass of the current subclass |
| 5 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 6 | `PRIVATE_IND` | DOUBLE |  |  | The Private_Ind indicates if the interesting case is a shared case or a private case. |
| 7 | `SUBCLASS_DISPLAY_SEQ` | DOUBLE | NOT NULL |  | Identifies the order in which the subclass is to be displayed in interesting case subclass build. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PARENT_INT_CASE_ID` | [RAD_INT_CASE](RAD_INT_CASE.md) | `INT_CASE_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [RAD_INT_CASE](RAD_INT_CASE.md) | `PARENT_INT_CASE_ID` |
| [RAD_INT_CASE_R](RAD_INT_CASE_R.md) | `INT_CASE_ID` |

