# SPECIMEN_USAGE

> Contains usage event for a given specimen.

**Description:** specimen usage  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATED_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Container that was created to store the new specimen in. |
| 2 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely relates this row to a specific order. |
| 3 | `PARENT_CONTAINER_ID` | DOUBLE | NOT NULL | FK→ | Container the parent specimen was located in. |
| 4 | `PARENT_SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Parent specimen that was used in the creation of the specimen. |
| 5 | `SPECIMEN_ID` | DOUBLE | NOT NULL | FK→ | Specimen for which this usage event refers to. |
| 6 | `SPECIMEN_USAGE_ID` | DOUBLE | NOT NULL |  | Non-intelligent key to uniquely identify a row. |
| 7 | `UNITS_CD` | DOUBLE | NOT NULL |  | Units of measure for given volume. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `USAGE_DT_TM` | DATETIME | NOT NULL |  | The date and time this usage event occurred on. |
| 14 | `USAGE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for this usage event. |
| 15 | `VOLUME_USED_QTY` | DOUBLE | NOT NULL |  | Volume of parent container used to create the new specimen. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATED_CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PARENT_CONTAINER_ID` | [CONTAINER](CONTAINER.md) | `CONTAINER_ID` |
| `PARENT_SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |
| `SPECIMEN_ID` | [V500_SPECIMEN](V500_SPECIMEN.md) | `SPECIMEN_ID` |
| `USAGE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

