# CE_SUSCEPTIBILITY

> ce susceptibility

**Description:** ce susceptibility  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABNORMAL_FLAG` | DOUBLE | NOT NULL |  | Flag to identify abnormal results. |
| 2 | `ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | The type of antibiotic for microbiology susceptibility results. |
| 3 | `ANTIBIOTIC_NOTE` | VARCHAR(255) |  |  | Text note associated with susceptibility |
| 4 | `CHARTABLE_FLAG` | DOUBLE | NOT NULL |  | Flag to identify chartable results. |
| 5 | `DETAIL_SUSCEPTIBILITY_CD` | DOUBLE | NOT NULL |  | The details of the susceptibility testing. |
| 6 | `DILUENT_VOLUME` | DOUBLE | NOT NULL |  | The volume of diluent needed. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to the clinical event table. |
| 8 | `MICRO_SEQ_NBR` | DOUBLE | NOT NULL | FK→ | Combined with event_id to form foreign key to ce_microbiology |
| 9 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Resistance if result_cd is not used |
| 10 | `PANEL_ANTIBIOTIC_CD` | DOUBLE | NOT NULL |  | Descirbes the panel of antibiotics for microbiology susceptibility results. |
| 11 | `RESULT_CD` | DOUBLE | NOT NULL |  | The resistance of an organism to a particular antibiotic (susceptibility interpretation). |
| 12 | `RESULT_DT_TM` | DATETIME | NOT NULL |  | The date and time of the results. |
| 13 | `RESULT_NUMERIC_VALUE` | DOUBLE |  |  | The numeric value of the results. |
| 14 | `RESULT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Personnel ID of the person reporting the results. |
| 15 | `RESULT_TEXT_VALUE` | VARCHAR(100) |  |  | The free text description of the results. |
| 16 | `RESULT_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 17 | `RESULT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the susceptibility interpretation. |
| 18 | `SUSCEPTIBILITY_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the susceptibility. |
| 19 | `SUSCEPTIBILITY_TEST_CD` | DOUBLE | NOT NULL |  | The type of susceptibility testing done (MIC, Kirby-Bauer...). |
| 20 | `SUSCEP_SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence number to make the primary key unique, when there is more than one susceptibility test per growth. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when this row is valid. |
| 27 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL | FK→ | Contains the End Point of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EVENT_ID` | [CE_MICROBIOLOGY](CE_MICROBIOLOGY.md) | `EVENT_ID` |
| `MICRO_SEQ_NBR` | [CE_MICROBIOLOGY](CE_MICROBIOLOGY.md) | `MICRO_SEQ_NBR` |
| `RESULT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `VALID_UNTIL_DT_TM` | [CE_MICROBIOLOGY](CE_MICROBIOLOGY.md) | `VALID_UNTIL_DT_TM` |

