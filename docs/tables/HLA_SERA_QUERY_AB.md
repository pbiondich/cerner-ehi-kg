# HLA_SERA_QUERY_AB

> Defines antibody screen information relating to a specific sera on hla_sera_query_serum. All information conatined on this table is a snapshot from the time it was created.

**Description:** HLA Sera Query Antibody Screen Information  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AB_SEQ` | DOUBLE | NOT NULL |  | Sequentially assigned |
| 2 | `ANTIBODIES_LIST_TXT` | VARCHAR(4000) |  |  | Contains a list of antibodies. This field is a snapshot of the list of antibody's code value display when the record was saved. |
| 3 | `B_CELL_PRA` | DOUBLE |  |  | The b-cell pra for the serum. |
| 4 | `DILUTION` | CHAR(40) |  |  | The dilution for the serum. This field is a snapshot of the code value's display when the record was saved. |
| 5 | `METHODOLOGY` | CHAR(40) |  |  | The methodology for the serum. This field is a snapshot of the code value's display when the record was saved. |
| 6 | `OD_RATIO_VALUE` | DOUBLE | NOT NULL |  | Holds the od ratio value for antibody screen history. |
| 7 | `OD_VALUE` | DOUBLE | NOT NULL |  | Holds the od value for antibody screen history. |
| 8 | `REACTION` | CHAR(40) |  |  | The reaction for the serum. This field is a snapshot of the code value's display when the record was saved. |
| 9 | `SERA_QUERY_SERUM_ID` | DOUBLE | NOT NULL | FK→ | Identifies the sera query serum record to which this serum belongs. It is a foreign key reference to the primary key of the hla_sera_query_serum table. |
| 10 | `T_CELL_PRA` | DOUBLE |  |  | The T-Cell PRA for the serum. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERA_QUERY_SERUM_ID` | [HLA_SERA_QUERY_SERUM](HLA_SERA_QUERY_SERUM.md) | `SERA_QUERY_SERUM_ID` |

