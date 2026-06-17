# MIC_IC_ORDERS

> This activity table contains 'order' level information that is used for Infection Control Candidate reporting. This table contains information for General Lab and Microbiology orders only.

**Description:** Infection Control Candidate Orders  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | VARCHAR(20) | NOT NULL |  | This field uniquely identifies an order or a group of orders. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code for the 'type' of order. For example, this table contains orders for both General Lab and Microbiology procedures and this field is used to differentiate between the types. |
| 3 | `BODY_SITE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code identifying the body site from which this specimen was drawn. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the orderable procedure. This could be used to join to the ORDER_CATALOG table. |
| 5 | `COMPLETE_DT_TM` | DATETIME |  |  | This field contains the date and time at which the orderable procedure was completed. |
| 6 | `CULTURE_START_DT_TM` | DATETIME |  |  | This field identifies the start date and time of the orderable procedure. |
| 7 | `DRAWN_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which the orderable procedure was collected. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `NOSOCOMIAL_IND` | DOUBLE |  |  | This field indicates whether an infection was acquired during a hospital stay. Valid values include: 0 = No nosocomial infection 1 = Nosocomial infection |
| 10 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code assigned to each orderable procedure associated with an order. For example: if there are two procedures on the same accession number, then each procedure will have a unique order id. |
| 11 | `ORDER_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code for the ordering provider. This could be used to join to the PRSNL table. |
| 12 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 13 | `POSITIVE_IND` | DOUBLE |  |  | This field indicates whether or not the procedure is considered positive. Microbiology procedures are considered positive when a preliminary or final report is issued that includes a positive response or organism. Valid values include: 0 = Not positive 1 = Positive |
| 14 | `PROCEDURE_ORDER_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which the orderable procedure was ordered. |
| 15 | `RECEIVED_DT_TM` | DATETIME | NOT NULL |  | This field contains the date and time at which the orderable procedure was received. |
| 16 | `SOURCE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the source to which this specimen was drawn. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ORDER_PROVIDER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

