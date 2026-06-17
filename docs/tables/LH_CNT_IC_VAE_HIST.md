# LH_CNT_IC_VAE_HIST

> This table stores a history of VAE event type changes.

**Description:** LH_CNT_IC_VAE_HIST  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LH_CNT_IC_VAE_HIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_CNT_IC_VAE_HIST table. |
| 2 | `LH_CNT_IC_VAE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the LH_CNT_IC_VAE table. |
| 3 | `PERFORMED_BY_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who updated the vae_type_flag. |
| 4 | `PERFORMED_DT_TM` | DATETIME |  |  | The date/time the vae_type_flag was changed. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VAE_TYPE_FLAG` | DOUBLE | NOT NULL |  | The VAE event type/category from the LH_CNT_IC_VAE table.0 - Risk for VAE1 - VAC2 - IVAC3 - Possible VAP4 - Probable VAP5 - IVAC Patients with Positive Pleural Fluid Culture6 - IVAC Patients with Lung Histopathology Result7 - Patient Removed8 - No NHSN Event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LH_CNT_IC_VAE_ID` | [LH_CNT_IC_VAE](LH_CNT_IC_VAE.md) | `LH_CNT_IC_VAE_ID` |
| `PERFORMED_BY_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

